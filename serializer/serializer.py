from formatter import serialize_dict_json
from parser import pack, unpack


def dumps(obj):
    return serialize_dict_json(pack(obj), '')


def dump(obj, filepath):
    with open(filepath, 'w') as file:
        file.writelines(serialize_dict_json(pack(obj), ''))
