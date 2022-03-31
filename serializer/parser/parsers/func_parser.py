import types


def bury_func(func):
    """Parses function into dictionary format"""

    parsed = {}
    parsed['object_type'] = 'function'

    glob = func.__globals__
    code = func.__code__
    ATTRS = ['argcount', 'cellvars', 'code', 'consts', 'filename', 'firstlineno', 'flags',
             'freevars', 'kwonlyargcount', 'lnotab', 'name', 'names', 'nlocals', 'posonlyargcount',
             'stacksize', 'varnames']

    prefix = 'co_'
    for attr in ATTRS:
        parsed[attr] = code.__getattribute__(prefix+attr)
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

