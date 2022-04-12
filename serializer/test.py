from pprint import pprint
from traceback import print_tb
from deformatter import deserialize
from serializer import load, dump
from parser import pack, unpack
from unified_parser import bury_class, ressurect_class
from formatter import serialize_dict_json

G = 'dsdsds'


class Dummy():
    def __init__(self):
        print('GASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

    def big_boy(self):
        print("SIUUUUUUUUUUUUUUUUUUUU"+G)


dump(Dummy, './test.json')

a = load('./test.json')

b = a().big_boy()
