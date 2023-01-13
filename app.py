from flask import Flask

from aengine_flask.routers import Router
from aengine_flask.json_dict import JsonDict
from importlib import import_module


class App:
    __routers = {}
    app = Flask(__name__)
    config: JsonDict

    def add_router(self, router: Router):
        if isinstance(router.rules, str):
            self.__routers[router.rules] = router
        elif isinstance(router.rules, list):
            for rule in router.rules:
                self.__routers[rule] = router

    def add_routers(self, routers: list):
        for router in routers:
            self.add_router(router)

    def init(self):
        for k, v in self.__routers.items():
            router = v.to_dict()
            del router["rules"]
            self.app.add_url_rule(k, k, **router)

    def load_config(self, path):
        self.config = JsonDict(path)
        if self.config.get('screenImportPath'):
            import_path = self.config['screenImportPath'] + "."
        else:
            import_path = ""
        if self.config.get("routes"):
            if isinstance(self.config.routes, dict):
                for k, v in self.config.routes.items():
                    self.add_router(Router(k, import_module(f"{import_path}{v}").__getattribute__(v)()))

    def set_root_folder(self, path):
        self.app.root_path = path

    def run(self, *args, **kwargs):
        args = list(args)
        ip = args[0] if len(args) > 0 else kwargs["ip"] if kwargs.get("ip") else "127.0.0.1"
        if kwargs.get("ip"):
            del kwargs["ip"]
        port = args[1] if len(args) > 1 else kwargs["port"] if kwargs.get("port") else 5000
        if kwargs.get("port"):
            del kwargs["port"]
        self.init()
        self.app.run(ip, port, **kwargs)
