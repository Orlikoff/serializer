from hashlib import new
from importlib import import_module
import inspect
import types


BUILTIN_TYPES = ('int', 'str', 'bool', 'list',
                 'dict', 'tuple', 'getset_descriptor')

WASTE = ('__doc__', '__eq__', '__format__', '__ge__',
         '__getattribute__', '__gt__', '__hash__',
         '__le__', '__lt__', '__module__', '__ne__',
         '__reduce__', '__reduce_ex__', '__repr__',
         '__setattr__', '__sizeof__', '__subclasshook__',
         '__weakref__', '__delattr__', '__new__', '__dict__',
         'getset_descriptor')


def bury_func(func):
    """Parses function into dictionary format"""

    parsed = {}
    parsed['object_type'] = 'function'

    code = func.__code__
    ATTRS = ['argcount', 'cellvars', 'code', 'consts', 'filename', 'firstlineno', 'flags',
             'freevars', 'kwonlyargcount', 'lnotab', 'name', 'names', 'nlocals', 'posonlyargcount',
             'stacksize', 'varnames']

    prefix = 'co_'
    for attr in ATTRS:
        if attr in ('code', 'lnotab'):
            parsed[attr] = code.__getattribute__(prefix+attr).hex()
        elif attr == 'filename':
            parsed[attr] = 'filename'
        elif attr == 'firstlineno':
            parsed[attr] = '0'
        elif attr == 'consts':
            res = []
            for c in code.__getattribute__(prefix+attr):
                res.append((c, type(c).__name__))
            parsed[attr] = res
        else:
            parsed[attr] = code.__getattribute__(prefix+attr)

    # glob = {k: v for k, v in func.__globals__.items() if k in parsed['names']}
    glob = {}

    for k, v in func.__globals__.items():
        if k in parsed['names']:
            if type(v).__name__ == 'module':
                glob[k] = k
            else:
                glob[k] = v

    type_glob = {k: type(v).__name__ for k,
                 v in func.__globals__.items() if k in parsed['names']}

    parsed['globals'] = glob
    parsed['type_globals'] = type_glob

    return parsed


def ressurect_func(data_dict):
    """Rebuilds function from data dict"""

    consts = []
    for const in data_dict['consts']:
        if const[1] == "int":
            consts.append(int(const[0]))
        elif const[1] == "str":
            consts.append(str(const[0]))
        elif const[1] == "bool":
            consts.append(bool(const[0]))
        elif const[1] == "list":
            consts.append(list(const[0]))
        elif const[1] == "dict":
            consts.append(dict(const[0]))
        elif const[1] == "tuple":
            consts.append(tuple(const[0]))
        elif const[1] == 'NoneType':
            consts.append(None)

    new_func_code = types.CodeType(int(data_dict['argcount']),
                                   int(data_dict['posonlyargcount']),
                                   int(data_dict['kwonlyargcount']),
                                   int(data_dict['nlocals']),
                                   int(data_dict['stacksize']),
                                   int(data_dict['flags']),
                                   bytes.fromhex(data_dict['code']),
                                   tuple(consts),
                                   tuple(data_dict['names']),
                                   tuple(data_dict['varnames']),
                                   'filename',
                                   data_dict['name'],
                                   0,
                                   bytes.fromhex(data_dict['lnotab']),
                                   tuple(data_dict['freevars']),
                                   tuple(data_dict['cellvars'])
                                   )

    formatted_globals = {}

    for k, v in data_dict['globals'].items():
        t = data_dict['type_globals'][k]
        if t == "int":
            formatted_globals[k] = int(v)
        elif t == "str":
            formatted_globals[k] = str(v)
        elif t == "bool":
            formatted_globals[k] = bool(v)
        elif t == "list":
            formatted_globals[k] = list(v)
        elif t == "dict":
            formatted_globals[k] = dict(v)
        elif t == "tuple":
            formatted_globals[k] = tuple(v)
        elif t == 'module':
            formatted_globals[k] = import_module(k)

    return types.FunctionType(new_func_code, formatted_globals, 'new')


def bury_class(cls):
    """Parses class into dictionary format"""

    parsed = {}
    parsed['object_type'] = 'class'
    parsed['fields'], parsed['methods'], parsed['bases'] = {}, {}, {}

    for base in cls.__bases__:
        if not base.__name__ == 'object':
            parsed['bases'][base.__name__] = bury_class(base)

    class_data = cls.__dict__

    for name, value in class_data.items():
        if name in WASTE:
            continue
        if inspect.isfunction(value):
            parsed['methods'][name] = bury_func(value)
        elif type(value).__name__ not in BUILTIN_TYPES and not inspect.isclass(value):
            parsed['fields'][name] = (bury_object(value), 'class_type')
        else:
            parsed['fields'][name] = (value, type(value).__name__)

    return parsed


def ressurect_class(data):
    """Rebuilds class from data dict"""

    params = {}

    BASES = []

    for _, value in data['bases'].items():
        BASES.append(ressurect_class(value))

    for k, v in data['methods'].items():
        params[k] = ressurect_func(v)

    for k, v in data['fields'].items():
        if v[1] == "int":
            params[k] = int(v[0])
        elif v[1] == "str":
            params[k] = str(v[0])
        elif v[1] == "bool":
            params[k] = bool(v[0])
        elif v[1] == "list":
            params[k] = list(v[0])
        elif v[1] == "dict":
            params[k] = dict(v[0])
        elif v[1] == "tuple":
            params[k] = tuple(v[0])
        elif v[1] == 'class_type':
            params[k] = ressurect_object(v[0])

    new_class = type('new_class', tuple(BASES), params)

    return new_class


def bury_object(obj):
    """Parses object into dictionary format"""

    parsed = {}
    parsed['object_type'] = 'object'
    parsed['fields'], parsed['methods'], parsed['functions'],\
        parsed['classes'], parsed['objects'] = {}, {}, {}, {}, {}

    object_data = inspect.getmembers(obj)

    for name, value in object_data:
        if name in WASTE:
            continue

        if type(value).__name__ in BUILTIN_TYPES and name not in ('__dict__', '__module__'):
            parsed['fields'][name] = (value, type(value).__name__)
        elif inspect.ismethod(value):
            parsed['methods'][name] = bury_func(value)
        elif inspect.isfunction(value):
            parsed['functions'][name] = bury_func(value)

    return parsed


def ressurect_object(data):
    """Rebuilds object from data dict"""

    params = {}

    for k, v in data['methods'].items():
        params[k] = ressurect_func(v)

    functions = {}
    fields = {}

    for k, v in data['functions'].items():
        functions[k] = ressurect_func(v)

    for k, v in data['fields'].items():
        if v[1] == "int":
            fields[k] = int(v[0])
        elif v[1] == "str":
            fields[k] = str(v[0])
        elif v[1] == "bool":
            fields[k] = bool(v[0])
        elif v[1] == "list":
            fields[k] = list(v[0])
        elif v[1] == "dict":
            fields[k] = dict(v[0])
        elif v[1] == "tuple":
            fields[k] = tuple(v[0])

    list_of_attrs = params['__init__'].__code__.co_varnames
    args = [v for k, v in fields.items() if k in list_of_attrs and not k == 'self']
    full_attrs = {**fields, **params}

    new_class = type('new_class', (), full_attrs)
    new_object = new_class(*args)

    for k, v in functions.items():
        setattr(new_object, k, v)

    return new_object
