import argparse
from gendiff_pack import generate_diff
from gendiff_pack.gendiff_engine.gendiff import generate_diff_dict
from gendiff_pack.gendiff_engine.input_format_parser import parse_input_file
from gendiff_pack.gendiff_format.format_diff import format_diff_stylish

def gendiff_script():
    gendiff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format', help='set format of output', default='stylish')
    args = gendiff.parse_args()
    dict1 = parse_input_file(args.first_file)
    dict2 = parse_input_file(args.second_file)
    diff_dict = generate_diff_dict(dict1, dict2)
    if args.format == 'stylish':
        print(format_diff_stylish(diff_dict))
