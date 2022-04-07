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
            parsed[attr] = code.__getattribute__(
                prefix+attr).encode('utf-8').hex()
        else:
            parsed[attr] = code.__getattribute__(prefix+attr)

    glob = {k: v for k, v in func.__globals__.items() if k in parsed['names']}

    parsed['globals'] = glob

    return parsed


def ressurect_func(data_dict):
    """Rebuilds function from data dict"""

    new_func_code = types.CodeType(int(data_dict['argcount']),
                                   int(data_dict['posonlyargcount']),
                                   int(data_dict['kwonlyargcount']),
                                   int(data_dict['nlocals']),
                                   int(data_dict['stacksize']),
                                   int(data_dict['flags']),
                                   bytes.fromhex(data_dict['code']),
                                   tuple(data_dict['consts']),
                                   tuple(data_dict['names']),
                                   tuple(data_dict['varnames']),
                                   bytes.fromhex(
                                       data_dict['filename']).decode('utf-8'),
                                   data_dict['name'],
                                   int(data_dict['firstlineno']),
                                   bytes.fromhex(data_dict['lnotab']),
                                   tuple(data_dict['freevars']),
                                   tuple(data_dict['cellvars'])
                                   )

    return types.FunctionType(new_func_code, data_dict['globals'], 'new')


def bury_class(cls):
    """Parses class into dictionary format"""

    parsed = {}
    parsed['object_type'] = 'class'
    parsed['fields'], parsed['methods'] = {}, {}

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

    new_class = type('new_class', (), params)

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

    new_class = type('new_class', (), params)
    new_object = new_class()

    for k, v in data['functions'].items():
        setattr(new_object, k, ressurect_func(v))

    for k, v in data['fields'].items():
        if v[1] == "int":
            setattr(new_object, k, int(v[0]))
        elif v[1] == "str":
            setattr(new_object, k, str(v[0]))
        elif v[1] == "bool":
            setattr(new_object, k, bool(v[0]))
        elif v[1] == "list":
            setattr(new_object, k, list(v[0]))
        elif v[1] == "dict":
            setattr(new_object, k, dict(v[0]))
        elif v[1] == "tuple":
            setattr(new_object, k, tuple(v[0]))

    return new_object
