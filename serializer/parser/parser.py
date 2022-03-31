import inspect
from unified_parser import bury_func, ressurect_func, bury_class, ressurect_class, bury_object, ressurect_object


def pack(obj):
    if inspect.isfunction(obj):
        return bury_func(obj)
    elif inspect.isclass(obj):
        return bury_class(obj)
    elif obj in (int, str, bool, tuple, dict, list):
        pass
    else:
        return bury_object(obj)


def unpack(data):
    if data['object_type'] == 'function':
        return ressurect_func(data)
    elif data['object_type'] == 'class':
        return ressurect_class(data)
    elif data['object_type'] == 'object':
        return ressurect_object(data)
