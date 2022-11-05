from gendiff import generate_diff


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


def test_generate_diff_plain_format_with_plain_files():
    with open(
        'tests/fixtures/results/plain/result_with_plain_files.txt'
    ) as f:
        result = f.read()
        assert generate_diff(file1_json, file2_json, format_name='plain') == (
            result)
        assert generate_diff(file1_yml, file2_yaml, format_name='plain') == (
            result)
        assert generate_diff(file1_yml, file2_json, format_name='plain') == (
            result)
        assert generate_diff(file1_json, file2_yaml, format_name='plain') == (
            result)


def test_generate_diff_plain_format_with_nested_files():
    with open(
        'tests/fixtures/results/plain/result_with_nested_files.txt'
    ) as f:
        result = f.read()
        assert generate_diff(file1_nested_json, file2_nested_json,
                             format_name='plain') == result
        assert generate_diff(file1_nested_yml, file2_nested_yaml,
                             format_name='plain') == result
        assert generate_diff(file1_nested_yml, file2_nested_json,
                             format_name='plain') == result
        assert generate_diff(file1_nested_json, file2_nested_yaml,
                             format_name='plain') == result
