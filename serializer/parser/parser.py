import inspect
from parsers.func_parser import bury_func, ressurect_func


def pack(obj):
    if inspect.isfunction(obj):
        return bury_func(obj)

def unpack(data):
    if data['object_type'] == 'function':
        return ressurect_func(data)

