import json


def read_config(file_path):
    with open(file_path) as data_file:
        config = json.load(data_file)

    return config
