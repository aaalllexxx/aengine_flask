import os

from aengine_flask.json_dict import JsonDict

base_dir = os.path.dirname(os.path.realpath(__file__))
settings = JsonDict(base_dir + "/settings.json")
