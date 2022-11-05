import argparse


def get_args():
    gendiff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format', help='set format of output',
                         default='stylish',
                         choices=['stylish', 'plain', 'json'])
    args = gendiff.parse_args()
    return args
