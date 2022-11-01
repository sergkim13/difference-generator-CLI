from gendiff_pack.gendiff_engine.input_format_parser import parse_input_file
from pprint import pprint


def diff(source1, source2):
    keys = sorted(source1.keys() | source2.keys())
    result = {}
    for key in keys:
        if key not in source1:
            result[(key, 'added')] = source2[key]
        elif key not in source2:
            result[(key, 'deleted')] = source1[key]
        elif isinstance(source1[key], dict) and isinstance(source2[key], dict):
            result[key, 'children'] = diff(source1[key], source2[key])
        elif source1[key] == source2[key]:
            result[(key, 'unchanged')] = source1[key]
        else:
            result[(key, 'changed')] = (source1[key], source2[key])
    return result


def convert_bool(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def generate_diff_plain(path_to_file1, path_to_file2):
    dict1 = parse_input_file(path_to_file1)
    dict2 = parse_input_file(path_to_file2)
    keys = sorted(list(dict1.keys() | dict2.keys()))
    diff_list = []
    for key in keys:
        if key not in dict1:
            diff_list.append(f'+ {key} : {convert_bool(dict2[key])}')
        elif key not in dict2:
            diff_list.append(f'- {key} : {convert_bool(dict1[key])}')
        elif dict1[key] == dict2[key]:
            diff_list.append(f'  {key} : {convert_bool(dict1[key])}')
        else:
            diff_list.append(
                f'- {key} : {convert_bool(dict1[key])}\n'
                f'+ {key} : {convert_bool(dict2[key])}')
    diff_str = '\n'.join(diff_list)
    result = '{\n' + diff_str + '\n' + '}'
    return (result)

def generate_diff(path_to_file1, path_to_file2):
    dict1 = parse_input_file(path_to_file1)
    dict2 = parse_input_file(path_to_file2)
    result = format(diff(dict1, dict2))
    return result

# dict1 = parse_input_file('/Users/kimsergey/coding/python-project-50/tests/fixtures/nested/file1.json')
# dict2 = parse_input_file('/Users/kimsergey/coding/python-project-50/tests/fixtures/nested/file2.json')

# pprint(diff(dict1, dict2))