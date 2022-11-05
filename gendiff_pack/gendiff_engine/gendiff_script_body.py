import argparse
from gendiff_pack import generate_diff


def gendiff_script():
    gendiff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format', help='set format of output. '
                         'Available output formats:'
                         'stylish (default formatter); '
                         'plain (-f plain); '
                         'json (-f json)', default='stylish',
                         choices=['stylish', 'plain', 'json'])
    args = gendiff.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    format_name = args.format
    print(generate_diff(path_to_file1, path_to_file2, format_name=format_name))
