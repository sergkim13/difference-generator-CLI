from gendiff.gendiff_diff import make_diff_dict, parse_input_file


file1_json = 'tests/fixtures/plain_files/file1.json'
file2_json = 'tests/fixtures/plain_files/file2.json'
file1_yml = 'tests/fixtures/plain_files/file1.yml'
file2_yaml = 'tests/fixtures/plain_files/file2.yaml'

file1_nested_json = 'tests/fixtures/nested_files/file1.json'
file2_nested_json = 'tests/fixtures/nested_files/file2.json'
file1_nested_yml = 'tests/fixtures/nested_files/file1.yml'
file2_nested_yaml = 'tests/fixtures/nested_files/file2.yaml'


diff_dict = {
    ('common', 'children'): {
        ('follow', 'added'): False,
        ('setting1', 'unchanged'): 'Value 1',
        ('setting2', 'deleted'): 200,
        ('setting3', 'changed'): (True, None),
        ('setting4', 'added'): 'blah blah',
        ('setting5', 'added'): {'key5': 'value5'},
        ('setting6', 'children'): {
            ('doge', 'children'): {('wow', 'changed'): ('', 'so much')},
            ('key', 'unchanged'): 'value',
            ('ops', 'added'): 'vops'}},
    ('group1', 'children'): {
        ('baz', 'changed'): ('bas', 'bars'),
        ('foo', 'unchanged'): 'bar',
        ('nest', 'changed'): ({'key': 'value'}, 'str')},
    ('group2', 'deleted'): {'abc': 12345, 'deep': {'id': 45}},
    ('group3', 'added'): {'deep': {'id': {'number': 45}}, 'fee': 100500}}


def test_parsing_wrong_file():
    assert parse_input_file(
        'bad_example.doc') == 'This should be json or yaml file!'


def test_make_diff_nested1():
    dict1 = parse_input_file(file1_nested_json)
    dict2 = parse_input_file(file2_nested_json)
    assert make_diff_dict(dict1, dict2) == diff_dict


def test__make_diff_nested2():
    dict1 = parse_input_file(file1_nested_json)
    dict2 = parse_input_file(file2_nested_yaml)
    assert make_diff_dict(dict1, dict2) == diff_dict


def test_make_diff_nested3():
    dict1 = parse_input_file(file1_nested_yml)
    dict2 = parse_input_file(file2_nested_json)
    assert make_diff_dict(dict1, dict2) == diff_dict


def test_make_diff_nested4():
    dict1 = parse_input_file(file1_nested_yml)
    dict2 = parse_input_file(file2_nested_yaml)
    assert make_diff_dict(dict1, dict2) == diff_dict
