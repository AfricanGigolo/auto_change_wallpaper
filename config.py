import json
import os.path

from common import *

__CONFIG_FILE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
__CONFIG_FILE_NAME = "auto_change_wallpaper.data"


def __read_config():
    file_path = os.path.join(__CONFIG_FILE_DIR, __CONFIG_FILE_NAME)
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as f:
        try:
            content = json.load(f)
        except:
            content = {}
        return content


def set_config(config_dict):
    file_path = os.path.join(__CONFIG_FILE_DIR, __CONFIG_FILE_NAME)
    old_config = __read_config()
    new_config = dict(old_config, **config_dict)
    with open(file_path, "w") as f:
        json.dump(new_config, f)


def get_config():
    return __read_config()

