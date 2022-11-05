import json


def format_diff_json(source):

    def inner(current_value):
        if not isinstance(current_value, dict):
            return current_value

        json_dict = {}
        for key, val in current_value.items():
            if key[1] == 'changed':
                json_dict[f'- {key[0]}'] = inner(val[0])
                json_dict[f'+ {key[0]}'] = inner(val[1])
            else:
                json_dict[convert_keys(key)] = inner(val)
        return json_dict

    result = inner(source)
    return json.dumps(result, indent=4)


def convert_keys(key):
    keys_dict = {
        'added': "+ ",
        'deleted': '- ',
        'changed': '',
        'unchanged': '',
        'children': ''
    }
    return f'{keys_dict[key[1]]}{key[0]}' if isinstance(key, tuple) else key
