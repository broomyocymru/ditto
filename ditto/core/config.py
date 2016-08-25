import base64
import json
import os.path
from os.path import expanduser

from ditto.core import logger


def get(key):
    cls = DittoConfig()
    val = cls.get(key)
    return val


def not_set(key):
    cls = DittoConfig()
    val = cls.get(key)
    return val is None


def set(key, val):
    cls = DittoConfig()
    cls.set(key, val)


class DittoConfig:
    def __init__(self):
        self.config_path = os.path.abspath(os.path.join(expanduser("~"), ".ditto-cli"))
        self.get_config()

    def get_config(self):
        if not os.path.isfile(self.config_path):
            self.set_config({})

        config_file = open(self.config_path, "r")
        data = json.load(config_file)
        config_file.close()

        return data

    def set_config(self, config):
        config_file = open(self.config_path, 'w+')
        config_file.write(json.dumps(config, indent=4, sort_keys=True))
        config_file.close()

    def get(self, key):
        config = self.get_config()
        if key in config:
            return base64.b64decode(config[key])
        else:
            return None

    def set(self, key, value, overwrite=True):
        config = self.get_config()
        if overwrite or (key not in config):
            config[key] = base64.b64encode(value)
            self.set_config(config)

    def rm(self, key):
        config = dict(self.get_config())
        del config[key]
        self.set_config(config)

    def list(self):
        config = self.get_config()
        for key in config:
            logger.log(key + ': ' + self.get(key))
