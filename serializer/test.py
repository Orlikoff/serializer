from pickle import DUP
import pprint
from serializer import dumps, dump, load, loads
from parser import pack, unpack


class Dummy():
    foo = 1
    bar = 's'

    def __init__(self):
        print('SIUUUUUUUUUUUUUUUUUUUUU')

    def ass(self):
        print('hi')


dump(Dummy, './test.json')
data = load('./test.json')
data2 = pack(Dummy)
pprint.pprint(data)
pprint.pprint(data2)
