import inspect
import types


BUILTIN_TYPES = ('int', 'str', 'bool', 'list',
                 'dict', 'tuple', 'getset_descriptor')


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
        parsed[attr] = code.__getattribute__(prefix+attr)

    glob = {k: v for k, v in func.__globals__.items() if k in parsed['names']}

    parsed['globals'] = glob

    return parsed


def ressurect_func(data_dict):
    """Rebuilds function from data dict"""

    new_func_code = types.CodeType(data_dict['argcount'],
                                   data_dict['posonlyargcount'],
                                   data_dict['kwonlyargcount'],
                                   data_dict['nlocals'],
                                   data_dict['stacksize'],
                                   data_dict['flags'],
                                   data_dict['code'],
                                   data_dict['consts'],
                                   data_dict['names'],
                                   data_dict['varnames'],
                                   data_dict['filename'],
                                   data_dict['name'],
                                   data_dict['firstlineno'],
                                   data_dict['lnotab'],
                                   data_dict['freevars'],
                                   data_dict['cellvars']
                                   )

    return types.FunctionType(new_func_code, data_dict['globals'], 'new')


def bury_class(cls):
    """Parses class into dictionary format"""

    parsed = {}
    parsed['object_type'] = 'class'
    parsed['fields'], parsed['methods'] = {}, {}

    class_data = cls.__dict__

    for name, value in class_data.items():
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
