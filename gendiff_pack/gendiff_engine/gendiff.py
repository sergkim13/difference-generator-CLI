from gendiff_pack.gendiff_engine.input_format_parser import parse_input_file

def convert_bool(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    return value


def generate_diff(path_to_file1, path_to_file2):
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
