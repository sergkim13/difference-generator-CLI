def convert_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return f"'{value}'"


def get_property_name(parent, property):
    if parent == '':
        return f"'{property}'"
    else:
        return f"'{parent}.{property}'"


def get_line(key, name, val):
    if key == 'added':
        return f'Property {name} was added with value: {convert_value(val)}'
    elif key == 'deleted':
        return f'Property {name} was removed'
    else:
        return f'Property {name} was updated. '\
               f'From {convert_value(val[0])} to {convert_value(val[1])}'


def format_diff_plain(source):

    def inner(current_value, parent):
        lines = []
        for key, val in current_value.items():
            property_name = get_property_name(parent, key[0])
            if key[1] == 'children':
                lines.append(inner(val, key[0]))
            elif key[1] == 'unchanged':
                pass
            else:
                lines.append(get_line(key[1], property_name, val))
        return '\n'.join(lines)

    return inner(source, '')


diff_dict = {('common', 'children'): {('follow', 'added'): False,
                          ('setting1', 'unchanged'): 'Value 1',
                          ('setting2', 'deleted'): 200,
                          ('setting3', 'changed'): (True, None),
                          ('setting4', 'added'): 'blah blah',
                          ('setting5', 'added'): {'key5': 'value5'},
                          ('setting6', 'children'): {('doge', 'children'): {('wow', 'changed'): ('',
                                                                                                 'so '
                                                                                                 'much')},
                                                     ('key', 'unchanged'): 'value',
                                                     ('ops', 'added'): 'vops'}},
 ('group1', 'children'): {('baz', 'changed'): ('bas', 'bars'),
                          ('foo', 'unchanged'): 'bar',
                          ('nest', 'changed'): ({'key': 'value'}, 'str')},
 ('group2', 'deleted'): {'abc': 12345, 'deep': {'id': 45}},
 ('group3', 'added'): {'deep': {'id': {'number': 45}}, 'fee': 100500}}

print(format_diff_plain(diff_dict))