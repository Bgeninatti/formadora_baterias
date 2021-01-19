import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_config(base_dir=BASE_DIR):
    config_file = os.path.join(base_dir, 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file)
    return config
