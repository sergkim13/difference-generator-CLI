# from gendiff import generate_diff
from pprint import pprint
import sys
pprint(sys.path)


# file1 = 'gendiff/file1.json'
# file2 = 'gendiff/file2.json'
# result = """
# {
# - follow : False
#   host : hexlet.io
# - proxy : 123.234.53.22
# - timeout : 50
# + timeout : 20
# + verbose : True
# }
# """


# def test_generate_diff():
    # assert generate_diff(file1, file2) == result