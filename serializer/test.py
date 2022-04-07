from pprint import pprint
from types import new_class
from deformatter import deserialize
from serializer import load, dump
from unified_parser import bury_class, ressurect_class
from formatter import serialize_dict_json


class Dummy():
    def __init__(self):
        print('Ass')


# data = dump(Dummy, './test.json')
# new_cls = load('./test.json')

# a = new_cls()
a = ([1])

А как мне писать ЛР, если я не Senior Python Developer со
стажем работы 15000 лет? Более того, если я собираюсь клепать
сайтики со своими друзьями: 3
