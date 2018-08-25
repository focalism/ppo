import sys
import yaml


def get_config(config_file):
    with open(config_file, encoding="utf-8") as f:
        _config = yaml.load(f)
        if not isinstance(_config, dict):
            sys.exit(1)
        return _config