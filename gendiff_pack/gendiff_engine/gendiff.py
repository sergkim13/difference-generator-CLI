from gendiff_pack.gendiff_format.format_diff_stylish import format_diff_stylish
from gendiff_pack.gendiff_format.format_diff_plain import format_diff_plain
import json
import yaml


def parse_input_file(path_to_file):
    if path_to_file.endswith('.json'):
        return json.load(open(path_to_file))
    elif path_to_file.endswith('.yaml') or path_to_file.endswith('.yml'):
        return yaml.safe_load(open(path_to_file))
    else:
        return 'This should be json or yaml file!'


def make_diff_dict(source1, source2):
    keys = sorted(source1.keys() | source2.keys())
    result = {}
    for key in keys:
        if key not in source1:
            result[(key, 'added')] = source2[key]
        elif key not in source2:
            result[(key, 'deleted')] = source1[key]
        elif isinstance(source1[key], dict) and isinstance(source2[key], dict):
            result[key, 'children'] = make_diff_dict(source1[key], source2[key])
        elif source1[key] == source2[key]:
            result[(key, 'unchanged')] = source1[key]
        else:
            result[(key, 'changed')] = (source1[key], source2[key])
    return result


def generate_diff(path_to_file1, path_to_file2, format_name='stylish'):
    dict1 = parse_input_file(path_to_file1)
    dict2 = parse_input_file(path_to_file2)
    if format_name == 'plain':
        result = format_diff_plain(make_diff_dict(dict1, dict2))
    else:
        result = format_diff_stylish(make_diff_dict(dict1, dict2))
    return result
