import enum
from serializer.dumper_loader import *


class Languages(enum.IntEnum):
    JSON = 1
    TOML = 2
    YAML = 3


class Serializer():
    def __init__(self, language):
        if language == Languages.JSON:
            self.dump = dump_json
            self.load = load_json
            self.dumps = dumps_json
            self.loads = loads_json
        elif language == Languages.TOML:
            self.dump = dump_toml
            self.load = load_toml
            self.dumps = dumps_toml
            self.loads = loads_toml
        elif language == Languages.YAML:
            self.dump = dump_yaml
            self.load = load_yaml
            self.dumps = dumps_yaml
            self.loads = loads_yaml
