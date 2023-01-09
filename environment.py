from ast import literal_eval
from os import PathLike
from typing import Union
import json_dict

import dotenv
from enum import Enum


class DataTypes(Enum):
    int = 1
    float = 2
    str = 3
    auto = 4


class Environment:
    __convert_functions = {
        "int": int,
        "float": float,
        "str": str,
        "auto": literal_eval
    }

    def __init__(self, path: Union[str, PathLike]):
        self.values = dotenv.dotenv_values(path)
        items = self.values.items()
        for key, value in items:
            self.__dict__[key] = value

    def get_key(self, key):
        return literal_eval(self.__dict__[key])

    def __getattribute__(self, item):
        obj = super().__getattribute__(item)
        try:
            return literal_eval(obj)
        except (ValueError, SyntaxError):
            return obj

    def __getitem__(self, item):
        return self.__getattribute__(item)

    def __repr__(self):
        return json.dumps(self.values, indent=4)
