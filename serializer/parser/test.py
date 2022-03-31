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


# for k, v in Testing.__dict__.items():
#     print(f'{k} : {v}')

# print(Testing.__dict__)
# for k, v in pack(Testing).items():
#     pprint.pprint(f'{k} : {v}')

b = Testing()
b.MY_FANCY_DUCKING_ATTRIBUTE = 10


def say_hello_YAY(h):
    print('Hello '+h)


b.say_hello_YAY = say_hello_YAY


data = pack(b)
new_obj = unpack(data)
new_obj.say_hello_YAY('boi')
