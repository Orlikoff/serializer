from parser import pack, unpack
import types
import pprint


class Testing():
    a = 10
    string_data = 'Goodies'

    def __init__(self):
        print("I'm awake!")

    def _my_custom_method(self, a, b):
        return a*b


# for k, v in Testing.__dict__.items():
#     print(f'{k} : {v}')

# print(Testing.__dict__)
# for k, v in pack(Testing).items():
#     pprint.pprint(f'{k} : {v}')

data = pack(Testing)
new_class = unpack(data)

a = new_class()
print(a._my_custom_method(4, 5))
