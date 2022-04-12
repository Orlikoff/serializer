from pprint import pprint
from formatter import serialize_dict_json
from parser import pack, unpack
from deformatter import deserialize


def dumps_json(obj):
    return serialize_dict_json(pack(obj), '')


def dump_json(obj, filepath):
    with open(filepath, 'w') as file:
        file.writelines(serialize_dict_json(pack(obj), ''))


def loads_json(string):
    data = string.split('\n')
    return unpack(deserialize(data[1:len(data)-2]))


def load_json(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        return loads(data)
