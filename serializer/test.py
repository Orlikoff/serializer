from struct import unpack
from serializer import dumps, dump
from parser import pack, unpack


class T():
    def __init__(self) -> None:
        print('Ass')


class Test():
    lolich = 10
    dum = T()

    def __init__(self):
        print('AWAKE!')


dump(Test, './test.json')
