import os
from aengine_flask.app import App


class MyApp(App):
    def __init__(self):
        self.load_config("config.json")


if __name__ == "__main__":
    app = MyApp()
    app.set_root_folder(os.path.dirname(os.path.realpath(__file__)))
    app.run("127.0.0.1", 80, debug=True)
