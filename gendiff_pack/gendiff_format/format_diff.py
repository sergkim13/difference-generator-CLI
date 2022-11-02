import itertools


def convert_bool(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def format_diff(source, replacer=' ', spacesCount=2):

    def inner(current_value, depth):
        if not isinstance(current_value, dict):
            return convert_bool(current_value)

        current_indent = replacer * depth
        deep_indent_size = depth + spacesCount
        deep_indent = replacer * deep_indent_size
        lines = []
        for key, val in current_value.items():
            if key[1] == 'added':
                lines.append(f'{deep_indent}+ {key[0]}: '
                             f'{inner(val, deep_indent_size + 2)}')
            elif key[1] == 'deleted':
                lines.append(f'{deep_indent}- {key[0]}: '
                             f'{inner(val, deep_indent_size + 2)}')
            elif key[1] == 'changed':
                lines.append(
                    f'{deep_indent}- {key[0]}: '
                    f'{inner(val[0], deep_indent_size + 2)}\n'
                    f'{deep_indent}+ {key[0]}: '
                    f'{inner(val[1], deep_indent_size + 2)}')
            elif key[1] == 'unchanged':
                lines.append(f'{deep_indent}  {key[0]}: '
                             f'{inner(val, deep_indent_size + 2)}')
            elif key[1] == 'children':
                lines.append(f'{deep_indent}  {key[0]}: '
                             f'{inner(val, deep_indent_size + 2)}')
            else:
                lines.append(f'{deep_indent}  {key}: '
                             f'{inner(val, deep_indent_size + 2)}')
            result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(source, 0)
