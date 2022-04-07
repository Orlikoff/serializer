from pprint import pprint
from deformatter import deserialize
from serializer import load, dump
from parser import pack, unpack
from unified_parser import bury_class, ressurect_class
from formatter import serialize_dict_json


class Dummy():
    def __init__(self):
        print('GASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

    def big_boy(self):
        print("SIUUUUUUUUUUUUUUUUUUUU")


a = pack(Dummy)
A = unpack(a)
b = A().big_boy()
