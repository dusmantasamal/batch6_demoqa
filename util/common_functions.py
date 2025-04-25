import json
import os


def get_browser_name():
    file_path = os.path.join(get_parent_framework_path(),"data","input_data.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data["browser"].lower()


def get_data_from_input(data_key):
    file_path = os.path.join(get_parent_framework_path(),"data","input_data.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data[data_key]

def get_orange_url():
    file_path = os.path.join(get_parent_framework_path(),"data","input_data.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data["url"]

def get_parent_framework_path():
    current_path = os.getcwd()
    get_parent = os.path.dirname(current_path)
    return get_parent