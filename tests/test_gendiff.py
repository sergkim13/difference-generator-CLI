from gendiff_pack.gendiff_engine.gendiff import generate_diff_plain, diff, generate_diff
from gendiff_pack.gendiff_engine.input_format_parser import parse_input_file


file1_json = 'tests/fixtures/plain/file1.json'
file2_json = 'tests/fixtures/plain/file2.json'
file1_yml = 'tests/fixtures/plain/file1.yml'
file2_yaml = 'tests/fixtures/plain/file2.yaml'

file1_nested_json = 'tests/fixtures/nested/file1.json'
file2_nested_json = 'tests/fixtures/nested/file2.json'
file1_nested_yml = 'tests/fixtures/nested/file1.yml'
file2_nested_yaml = 'tests/fixtures/nested/file2.yaml'


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


def test_diff_nested1():
  dict1 = parse_input_file(file1_nested_json)
  dict2 = parse_input_file(file2_nested_json)
  assert diff(dict1, dict2) == diff_dict


def test_diff_nested2():
  dict1 = parse_input_file(file1_nested_json)
  dict2 = parse_input_file(file2_nested_yaml)
  assert diff(dict1, dict2) == diff_dict


def test_diff_nested3():
  dict1 = parse_input_file(file1_nested_yml)
  dict2 = parse_input_file(file2_nested_json)
  assert diff(dict1, dict2) == diff_dict


def test_diff_nested4():
  dict1 = parse_input_file(file1_nested_yml)
  dict2 = parse_input_file(file2_nested_yaml)
  assert diff(dict1, dict2) == diff_dict


def test_plain_generate_diff():
  with open('tests/fixtures/plain/result.txt') as f:
    result = f.read()
    assert generate_diff_plain(file1_json, file2_json) == result    
    assert generate_diff_plain(file1_yml, file2_yaml) == result
    assert generate_diff_plain(file1_yml, file2_json) == result
    assert generate_diff_plain(file1_json, file2_yaml) == result


def test_nested_generate_diff():
  with open('tests/fixtures/nested/result.txt') as f:
    result = f.read()
    assert generate_diff(file1_nested_json, file2_nested_json) == result
    assert generate_diff(file1_nested_yml, file2_nested_yaml) == result
    assert generate_diff(file1_nested_yml, file2_nested_json) == result
    assert generate_diff(file1_nested_json, file2_nested_yaml) == result
