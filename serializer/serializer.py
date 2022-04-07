from formatter import serialize_dict_json
from parser import pack, unpack
from deformatter import deserialize


def dumps(obj):
    return serialize_dict_json(pack(obj), '')


def dump(obj, filepath):
    with open(filepath, 'w') as file:
        file.writelines(serialize_dict_json(pack(obj), ''))


def loads(string):
    # return deserialize(string)
    return unpack(deserialize(string))


def load(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
        return loads(data[1:len(data)-1])
