import math
import unittest
from serializer.parser import pack, unpack
from data_for_tests import *

# Globals for testing
G = 10


# Functions for testing
def dummy_func_1(var1, var2):
    return var1 + var2


def dummy_func_2(var1, var2):
    return var1 + var2 + math.pi + G


# Classes for testing
class Dummy1():
    def __init__(self):
        print('Awake!')

    def greetings(self):
        return True


class Dummy2():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def greetings_imroved(self, a):
        return self.a + self.b + a


# Objects for testing
dummy_obj_1 = Dummy1()
dummy_obj_1.dummy_arg = 'dummy'

dummy_obj_2 = Dummy2(1, 2)
dummy_obj_2.dummy_arg = dummy_func_2


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


unittest.main()
