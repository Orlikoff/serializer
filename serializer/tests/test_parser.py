import math
import unittest
from serializer.parser import pack, unpack
from serializer.tests.data_for_tests import *


class TestParser(unittest.TestCase):
    def test_pack(self):
        self.assertEqual(pack(dummy_func_1), bury_func_case_1)
        self.assertEqual(pack(dummy_func_2), bury_func_case_2)
        self.assertEqual(pack(Dummy1), bury_class_case_1)
        self.assertEqual(pack(Dummy2), bury_class_case_2)
        self.assertEqual(pack(dummy_obj_1), bury_object_case_1)
        self.assertEqual(pack(dummy_obj_2), bury_object_case_2)

    def test_unpack(self):
        self.assertEqual(unpack(bury_func_case_1)(1, 2), 3)
        self.assertEqual(unpack(bury_func_case_2)(1, 2), math.pi+13)
        self.assertEqual(unpack(bury_class_case_1)().greetings(), True)
        self.assertEqual(unpack(bury_class_case_2)
                         (1, 2).greetings_imroved(3), 6)
        self.assertEqual(unpack(bury_object_case_1).greetings(), True)
        self.assertEqual(unpack(bury_object_case_1).dummy_arg, 'dummy')
        self.assertEqual(unpack(bury_object_case_2).greetings_imroved(3), 6)
        self.assertEqual(
            unpack(bury_object_case_2).dummy_arg(1, 2), math.pi+13)


if __name__ == '__main__':
    unittest.main()
