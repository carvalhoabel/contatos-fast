import json
from json import JSONDecodeError
from pathlib import Path
from os import mkdir
from os.path import (
    isdir, isfile
)


FILENAME = 'conftest.json'
ROOTDIR = 'contatos-fast'


def currentdir() -> str:
    return Path(__file__).parent.absolute().__str__()


def to_root_dir() -> str:
    direct = currentdir()
    return direct[: direct.index(ROOTDIR) + len(ROOTDIR)]


def to_settings() -> str:
    return f'{to_root_dir()}/settings'


def json_filepath() -> str:
    return f'{to_settings()}/conftest.json'


def config_file() -> str:
    if not isdir(to_settings()):
        mkdir(to_settings())
    return json_filepath()


def get_template() -> dict:
    return {
        'testing': False,
        'database': 'dbcontatos',
        'dbtest': 'dbcontatos_test',
    }


def create_conftest() -> dict:
    try:
        with open(file=config_file(), mode='r') as reader:
            json.loads(reader.read())
    except (JSONDecodeError, FileNotFoundError):
        with open(file=config_file(), mode='w') as writer:
            writer.write(json.dumps(get_template(), indent=4))
    finally:
        with open(file=config_file(), mode='r') as reader:
            json_data = json.loads(reader.read())
        return json_data


# activing test

def active_test() -> bool:
    try:
        json_data = create_conftest()
        if not json_data['testing']:
            json_data['testing'] = True
            with open(file=config_file(), mode='w') as writer:
                writer.write(json.dumps(json_data, indent=4))
    finally:
        del json_data
        return True


# deactiving test

def deactive_test() -> bool:
    try:
        json_data = create_conftest()
        if json_data['testing']:
            json_data['testing'] = False
            with open(file=config_file(), mode='w') as writer:
                writer.write(json.dumps(json_data, indent=4))
    finally:
        del json_data
        return True
