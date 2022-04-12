from serializer.formatter import serialize_dict_json, serialize_dict_toml, serialize_dict_yaml
from serializer.parser import pack, unpack
from serializer.deformatter import deserialize


def dumps_json(obj):
    return serialize_dict_json(pack(obj), '')


def dump_json(obj, filepath):
    with open(filepath, 'w') as file:
        file.writelines(dumps_json(obj))


def loads_json(string):
    data = string.split('\n')
    return unpack(deserialize(data[1:len(data)-2]))


def load_json(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        return loads_json(data)


def dumps_toml(obj):
    return serialize_dict_toml(pack(obj), '')


def dump_toml(obj, filepath):
    with open(filepath, 'w') as file:
        file.writelines(dumps_toml(obj))


def loads_toml(string):
    data = string.split('\n')
    return unpack(deserialize(data[5:len(data)-3]))


def load_toml(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        return loads_toml(data)


def dumps_yaml(obj):
    return serialize_dict_yaml(pack(obj), '')


def dump_yaml(obj, filepath):
    with open(filepath, 'w') as file:
        file.writelines(dumps_yaml(obj))


def loads_yaml(string):
    data = string.split('\n')
    return unpack(deserialize(data[2:len(data)-3]))


def load_yaml(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        return loads_yaml(data)
