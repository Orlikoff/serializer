import math
from pprint import pprint
from serializer import loads_json, dumps_json, load_json, dump_json

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
        print(math.sin(self.a))


a = AttrTest(4, 5)
data = dumps_json(a)

b = loads_json(data).lul()
