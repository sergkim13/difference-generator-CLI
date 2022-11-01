import itertools
from gendiff_pack.gendiff_engine.input_format_parser import parse_input_file


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

dict1 = parse_input_file('/Users/kimsergey/coding/python-project-50/tests/fixtures/nested/file1.json')
dict2 = parse_input_file('/Users/kimsergey/coding/python-project-50/tests/fixtures/nested/file2.json')

diff_dict = diff(dict1, dict2)

def convert_bool(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def format_diff(source, replacer='*', spacesCount=2):

    def inner(current_value, depth):
        if not isinstance(current_value, dict):
            return convert_bool(current_value)

        current_indent = replacer * depth # ' ' * 0 = 0 
        deep_indent_size = depth + spacesCount # 0 + 2 = 2
        deep_indent = replacer * deep_indent_size # ' ' * 2 = '  '
        lines = []
        for key, val in current_value.items():
            if key[1] == 'added':
                lines.append(f'{deep_indent}+ {key[0]}: {inner(val, deep_indent_size)}')
            elif key[1] == 'deleted':
                lines.append(f'{deep_indent}- {key[0]}: {inner(val, deep_indent_size)}')
            elif key[1] == 'changed':
                lines.append(
                    f'{deep_indent}- {key[0]}: {inner(val[0], deep_indent_size)}\n'
                    f'{deep_indent}+ {key[0]}: {inner(val[1], deep_indent_size)}')
            elif key[1] == 'unchanged':
                lines.append(f'{deep_indent}  {key[0]}: {inner(val, deep_indent_size)}')
            elif key[1] == 'children':
                lines.append(f'{deep_indent}  {key[0]}: {inner(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}  {key}: {inner(val, deep_indent_size)}')
            result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(source, 0)


print(format_diff(diff_dict))