from gendiff_pack.gendiff_engine.gendiff import generate_diff


file1 = '/Users/kimsergey/coding/python-project-50/tests/file1.json'
file2 = '/Users/kimsergey/coding/python-project-50/tests/file2.json'
result = """{
- follow : false
  host : hexlet.io
- proxy : 123.234.53.22
- timeout : 50
+ timeout : 20
+ verbose : true
}"""


def test_generate_diff():
    assert generate_diff(file1, file2) == result
