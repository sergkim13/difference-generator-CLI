import itertools


def convert_bool(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def get_prefix(key, indent):
    if key[1] == 'added':
        return f'{indent}+ {key[0]}: '
    elif key[1] == 'deleted':
        return f'{indent}- {key[0]}: '
    elif key[1] == 'unchanged' or key[1] == 'children':
        return f'{indent}  {key[0]}: '
    else:                            # если key не является кортежем,
        return f'{indent}  {key}: '  # значит val уже не рекурсивный случай


def format_diff_stylish(source, replacer=' ', spacesCount=2):

    def inner(current_value, depth):
        if not isinstance(current_value, dict):
            return convert_bool(current_value)

        current_indent = replacer * depth
        indent_size = depth + spacesCount
        indent = replacer * indent_size
        lines = []
        for key, val in current_value.items():
            if key[1] == 'changed':  # т.к. при 'changed' выводится 2 строки,
                lines.append(        # под этот случай выделен отдельный блок if
                    f'{indent}- {key[0]}: '
                    f'{inner(val[0], indent_size + 2)}\n'
                    f'{indent}+ {key[0]}: '
                    f'{inner(val[1], indent_size + 2)}')
            else:
                lines.append(f'{get_prefix(key, indent)}'
                             f'{inner(val, indent_size + 2)}')
            result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(source, 0)
