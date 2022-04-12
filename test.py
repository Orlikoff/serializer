import os
import math
from serializer.serializer_tools import Serializer, Languages


class Dummy():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def lul(self):
        math.sin(self.a+self.b)


json_s = Serializer(Languages.JSON)
json_s.dump(Dummy(4, 5), './a.json')
