import os


def get_env_bool(key, default):
    return bool(int(os.environ.get(key, default)))
