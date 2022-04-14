import os
from pprint import pprint
from tempfile import TemporaryFile
import unittest
from serializer.serializer_tools import Languages, Serializer
from tests.data_for_tests import *


class TestSerializerTools(unittest.TestCase):
    def test_Languages(self):
        self.assertEqual(Languages.JSON, 1)
        self.assertEqual(Languages.TOML, 2)
        self.assertEqual(Languages.YAML, 3)

    def test_JSON_Serializer_strings(self):
        serializer = Serializer(Languages.JSON)
        string_data = serializer.dumps(dummy_obj_2)
        obj2 = serializer.loads(string_data)
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)

    def test_TOML_Serializer_strings(self):
        serializer = Serializer(Languages.TOML)
        string_data = serializer.dumps(dummy_obj_2)
        obj2 = serializer.loads(string_data)
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)

    def test_YAML_Serializer_strings(self):
        serializer = Serializer(Languages.YAML)
        string_data = serializer.dumps(dummy_obj_2)
        obj2 = serializer.loads(string_data)
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)

    def test_JSON_Serializer_files(self):
        serializer = Serializer(Languages.JSON)
        serializer.dump(dummy_obj_2, 'test.json')
        obj2 = serializer.load('test.json')
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)
        os.remove('test.json')

    def test_TOML_Serializer_files(self):
        serializer = Serializer(Languages.TOML)
        serializer.dump(dummy_obj_2, 'test.toml')
        obj2 = serializer.load('test.toml')
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)
        os.remove('test.toml')

    def test_YAML_Serializer_files(self):
        serializer = Serializer(Languages.YAML)
        serializer.dump(dummy_obj_2, 'test.yaml')
        obj2 = serializer.load('test.yaml')
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)
        os.remove('test.yaml')


if __name__ == '__main__':
    unittest.main()
