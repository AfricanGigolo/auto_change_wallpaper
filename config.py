import json
import os.path

from common import *

__CONFIG_FILE_DIR = "./assets"
__CONFIG_FILE_NAME = "config.json"


def __read_config():
    file_path = get_resource_path(os.path.join(__CONFIG_FILE_DIR, __CONFIG_FILE_NAME))
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        content = json.load(f)
        return content


def set_config(config_dict):
    file_path = get_resource_path(os.path.join(__CONFIG_FILE_DIR, __CONFIG_FILE_NAME))
    old_config = __read_config()
    new_config = dict(old_config, **config_dict)
    with open(file_path, "w") as f:
        json.dump(new_config, f)


def get_config():
    return __read_config()

