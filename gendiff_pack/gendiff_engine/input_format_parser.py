import json
import yaml


def parse_input_file(path_to_file):
    if path_to_file.endswith('.json'):
        dict_ = json.load(open(path_to_file))
    elif path_to_file.endswith('.yml') or path_to_file.endswith('.yaml'):
        dict_ = yaml.safe_load(open(path_to_file))
    return dict_