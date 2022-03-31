import inspect
from unified_parser import bury_func, ressurect_func, bury_class, ressurect_class


def pack(obj):
    if inspect.isfunction(obj):
        return bury_func(obj)
    elif inspect.isclass(obj):
        return bury_class(obj)


def unpack(data):
    if data['object_type'] == 'function':
        return ressurect_func(data)
    elif data['object_type'] == 'class':
        return ressurect_class(data)
