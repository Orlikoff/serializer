import math
import unittest
from copy import deepcopy
from data_for_tests import *
from serializer.unified_parser import bury_func, bury_object, ressurect_func,\
    bury_class, ressurect_class, ressurect_object

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


class TestUnifiedParser(unittest.TestCase):
    def test_bury_func_1(self):
        buried = bury_func(dummy_func_1)
        test_data = deepcopy(bury_func_case_1)
        self.assertEqual(buried, test_data)

    def test_bury_func_2(self):
        buried = bury_func(dummy_func_2)
        test_data = deepcopy(bury_func_case_2)
        self.assertEqual(buried, test_data)

    def test_ressurect_func_1(self):
        func1 = ressurect_func(bury_func_case_1)
        self.assertEqual(func1(1, 2), 3)

    def test_ressurect_func_2(self):
        func2 = ressurect_func(bury_func_case_2)
        self.assertEqual(func2(1, 2), math.pi+13)

    def test_bury_class_1(self):
        buried = bury_class(Dummy1)
        test_data = deepcopy(bury_class_case_1)
        self.assertEqual(buried, test_data)

    def test_bury_class_2(self):
        buried = bury_class(Dummy2)
        test_data = deepcopy(bury_class_case_2)
        self.assertEqual(buried, test_data)

    def test_ressurect_class_1(self):
        class1 = ressurect_class(bury_class_case_1)
        test_class = class1()
        self.assertEqual(test_class.greetings(), True)

    def test_ressurect_class_2(self):
        class2 = ressurect_class(bury_class_case_2)
        test_class = class2(1, 2)
        self.assertEqual(test_class.greetings_imroved(3), 6)

    def test_bury_object_1(self):
        buried = bury_object(dummy_obj_1)
        test_data = deepcopy(bury_object_case_1)
        self.assertEqual(buried, test_data)

    def test_bury_object_2(self):
        buried = bury_object(dummy_obj_2)
        test_data = deepcopy(bury_object_case_2)
        self.assertEqual(buried, test_data)

    def test_ressurect_object_1(self):
        obj1 = ressurect_object(bury_object_case_1)
        self.assertEqual(obj1.greetings(), True)
        self.assertEqual(obj1.dummy_arg, 'dummy')

    def test_ressurect_object_2(self):
        obj2 = ressurect_object(bury_object_case_2)
        self.assertEqual(obj2.greetings_imroved(3), 6)
        self.assertEqual(obj2.dummy_arg(1, 2), math.pi+13)


unittest.main()
