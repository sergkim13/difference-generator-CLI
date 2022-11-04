def convert_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return f"'{value}'"


def get_property_name(parent, property):
    if parent == '':
        property_name = property
    else:
        property_name = f'{parent}.{property}'
    return property_name


def get_line(key, name, val):
    if key == 'added':
        return f"Property '{name}' was added with value: {convert_value(val)}"
    elif key == 'deleted':
        return f"Property '{name}' was removed"
    else:
        return f"Property '{name}' was updated. "\
               f"From {convert_value(val[0])} to {convert_value(val[1])}"


def format_diff_plain(source):

    def inner(current_value, parent):
        lines = []
        for key, val in current_value.items():
            property_name = get_property_name(parent, key[0])
            if key[1] == 'children':
                lines.append(inner(val, property_name))
            elif key[1] == 'unchanged':
                pass
            else:
                lines.append(get_line(key[1], property_name, val))
        return '\n'.join(lines)

    return inner(source, '')
