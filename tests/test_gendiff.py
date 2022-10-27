from gendiff_pack.gendiff_engine.gendiff import generate_diff


file1_json = 'tests/fixtures/plain/file1.json'
file2_json = 'tests/fixtures/plain/file2.json'
file1_yml = 'tests/fixtures/plain/file1.yml'
file2_yaml = 'tests/fixtures/plain/file2.yaml'

def test_plain_generate_diff():
  with open('tests/fixtures/plain/result.txt') as f:
    result = f.read()
    assert generate_diff(file1_json, file2_json) == result    
    assert generate_diff(file1_yml, file2_yaml) == result
    assert generate_diff(file1_yml, file2_json) == result
    assert generate_diff(file1_json, file2_yaml) == result