from importlib import import_module

from flask import Flask

from aengine_flask.json_dict import JsonDict
from aengine_flask.routers import Router


class App:
    __routers = {}
    app = Flask(__name__)
    config: JsonDict
    port = 5000
    ip = "127.0.0.1"
    debug = 0

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
                    screen = import_module(f"{import_path}{v}").__getattribute__(v)()
                    if hasattr(screen, "options"):
                        options = screen.options
                    else:
                        options = {}
                    self.add_router(Router(k, screen, **options))
        if self.config.get("ip"):
            self.ip = self.config.ip
        if self.config.get("port"):
            self.port = self.config.port
        if self.config.get("debug"):
            self.debug = self.config.debug

    def set_root_folder(self, path):
        self.app.root_path = path

    def run(self, *args, **kwargs):
        args = list(args)
        ip = args[0] if len(args) > 0 else kwargs["ip"] if kwargs.get("ip") else self.ip
        if kwargs.get("ip"):
            del kwargs["ip"]
        port = args[1] if len(args) > 1 else kwargs["port"] if kwargs.get("port") else self.port
        if kwargs.get("port"):
            del kwargs["port"]
        self.init()
        kwargs["debug"] = self.debug
        self.app.run(ip, port, **kwargs)
