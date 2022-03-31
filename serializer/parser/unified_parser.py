import inspect
import types


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
    parsed = {}
    parsed['object_type'] = 'class'
    parsed['fields'], parsed['methods'] = {}, {}

    class_data = cls.__dict__

    for name, value in class_data.items():
        if type(value) in (int, str, bool, list, dict, tuple):
            parsed['fields'][name] = [value, str(type(value))]
        elif inspect.isfunction(value):
            parsed['methods'][name] = bury_func(value)

    return parsed


def ressurect_class(data):
    params = {}

    for k, v in data['fields'].items():
        if v[1] == 'int':
            params[k] = int(v[0])
        elif v[1] == 'str':
            params[k] = str(v[0])
        elif v[1] == 'bool':
            params[k] = bool(v[0])
        elif v[1] == 'list':
            params[k] = list(v[0])
        elif v[1] == 'dict':
            params[k] = dict(v[0])
        elif v[1] == 'tuple':
            params[k] = tuple(v[0])

    for k, v in data['methods'].items():
        params[k] = ressurect_func(v)

    new_class = type('new_class', (), params)

    return new_class
