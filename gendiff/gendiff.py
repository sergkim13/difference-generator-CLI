import argparse
import json


def generate_diff(path_to_file1, path_to_file2):
    with open(path_to_file1) as f1:
        dict1 = json.load(f1)
    with open(path_to_file2) as f2:
        dict2 = json.load(f2)
    keys = sorted(list(dict1.keys() | dict2.keys()))
    diff_list = []
    for key in keys:
        if key not in dict1:
            diff_list.append(f'+ {key} : {dict2[key]}')
        elif key not in dict2:
            diff_list.append(f'- {key} : {dict1[key]}')
        elif dict1[key] == dict2[key]:
            diff_list.append(f'  {key} : {dict1[key]}')
        else:
            diff_list.append(f'- {key} : {dict1[key]}\n+ {key} : {dict2[key]}')
    diff_str = '\n'.join(diff_list)
    result = '{\n' + diff_str +'\n' + '}' 
    print(result)
    

file1 = 'gendiff/file1.json'
file2 = 'gendiff/file2.json'

generate_diff(file1, file2)

# def gendiff():
#     gendiff = argparse.ArgumentParser(description = 'Compares two configuration files and shows a difference.')
#     gendiff.add_argument('first_file')
#     gendiff.add_argument('second_file')
#     gendiff.add_argument('-f', '--format', help = 'set format of output')
#     args = gendiff.parse_args()
#     print(args.echo)