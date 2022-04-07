from struct import unpack
from serializer import dumps, dump
from parser import pack, unpack


class T():
    pass


class Test():
    lolich = 10
    dum = T()

    def __init__(self):
        print('AWAKE!')


test = pack(Test)
obj = unpack(test)

dump(Test, './test.json')

a = obj()
print(a.lolich)
