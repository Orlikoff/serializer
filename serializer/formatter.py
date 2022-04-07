import inspect

INDENT = 0


def tab():
    global INDENT
    INDENT += 1


def stab():
    global INDENT
    INDENT -= 1


def indent(string):
    global INDENT
    return '\t'*INDENT + string


def serialize_list_json(data, base_string):
    string = ''
    string += '[\n'
    tab()

    for element in data:
        if type(element) in (list, tuple):
            string += indent(f'{serialize_list_json(element, string)}')
        elif type(element) is dict:
            string += indent(f'{serialize_dict_json(element, string)}')
        else:
            string += indent(f'"{str(element)}"'+',\n')

    stab()
    string += indent('],\n')

    return string


def serialize_dict_json(data, base_string):
    string = ''
    string += '{\n'
    tab()

    for k, v in data.items():
        if type(v) in (list, tuple):
            string += indent(f'"{str(k)}": {serialize_list_json(v, string)}')
        elif type(v) is dict:
            string += indent(f'"{str(k)}": {serialize_dict_json(v, string)}')
        else:
            string += indent(f'"{str(k)}": "{str(v)}", \n')

    stab()
    string += indent('},\n')

    return string
