from gendiff_pack.gendiff_engine.gendiff import generate_diff


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'


def test_generate_diff():
  with open('tests/fixtures/result.txt') as f:
    result = f.read()
    assert generate_diff(file1, file2) == result    
