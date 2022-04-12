import json
import math
from serializer import Languages, Serializer

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
        print(math.sin(self.a+self.b))


a = AttrTest(4, 5)

json_serializer = Serializer(Languages.JSON)
json_serializer.dump(a, './test.json')
