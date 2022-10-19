import argparse


def gendiff_script():
    gendiff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')
    gendiff.add_argument('-f', '--format', help='set format of output')
    args = gendiff.parse_args()
    print(args.echo)
