from gendiff import generate_diff
import json

# Плоские файлы
file1_json = 'tests/fixtures/plain_files/file1.json'
file2_json = 'tests/fixtures/plain_files/file2.json'
file1_yml = 'tests/fixtures/plain_files/file1.yml'
file2_yaml = 'tests/fixtures/plain_files/file2.yaml'

# Вложенные файлы
file1_nested_json = 'tests/fixtures/nested_files/file1.json'
file2_nested_json = 'tests/fixtures/nested_files/file2.json'
file1_nested_yml = 'tests/fixtures/nested_files/file1.yml'
file2_nested_yaml = 'tests/fixtures/nested_files/file2.yaml'


def test_generate_diff_json_format_with_plain_files():
    result = json.load(open('tests/fixtures/results/json_format/json_format_result_with_plain_files.json'))
    result = json.dumps(result, indent=4)
    assert generate_diff(file1_json, file2_json, format_name='json') == result
    assert generate_diff(file1_yml, file2_yaml, format_name='json') == result
    assert generate_diff(file1_yml, file2_json, format_name='json') == result
    assert generate_diff(file1_json, file2_yaml, format_name='json') == result


def test_generate_diff_json_format_with_nested_files():
    result = json.load(open('tests/fixtures/results/json_format/json_format_result_with_nested_files.json'))
    result = json.dumps(result, indent=4)
    assert generate_diff(file1_nested_json, file2_nested_json, format_name='json') == result
    assert generate_diff(file1_nested_yml, file2_nested_yaml, format_name='json') == result
    assert generate_diff(file1_nested_yml, file2_nested_json, format_name='json') == result
    assert generate_diff(file1_nested_json, file2_nested_yaml, format_name='json') == result