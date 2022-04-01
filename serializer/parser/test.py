from random import random
from parser import pack, unpack
import inspect
import pprint


class Testing():
    a = 10
    string_data = 'Goodies'

    def __init__(self):
        print("I'm awake!")

    def _my_custom_method(self, a, b):
        return a*b


b = Testing()
b.MY_FANCY_DUCKING_ATTRIBUTE = {
    k: v for k, v in zip(range(0, 10), range(9, 19))}


def say_hello_YAY(h):
    print('Hello '+h)


class Boy():
    ass = 10
    str_ass = Testing()

    def greet():
        print("I'm BOYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")


b.say_hello_YAY = say_hello_YAY


data = pack(Boy)
new_obj = unpack(data)
print(new_obj.ass)
print(new_obj.str_ass._my_custom_method(5, 10))
