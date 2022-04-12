from pprint import pprint
from deformatter import deserialize
from serializer import load, dump
from parser import pack, unpack
from unified_parser import bury_class, ressurect_class
from formatter import serialize_dict_json

G = 'dsdsds'


class DUM():
    def say(self, a, b):
        print('lol')


class Dummy(DUM):
    def __init__(self):
        print('GASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

    def big_boy(self):
        print("SIUUUUUUUUUUUUUUUUUUUU"+G)


class AttrTest():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('gf')

    def lul(self):
        print(self.a+self.b)


a = AttrTest(4, 5)
dump(a, './test.json')

b = load('./test.json')
b.lul()
