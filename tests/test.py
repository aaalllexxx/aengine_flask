from app import App
from routers import Router
from screen import Screen


class HomeScreen(Screen):
    def main(self):
        return "Home Screen"


class MyApp(App):
    def __init__(self):
        self.add_routers([
            Router(["/", "/index"], HomeScreen(), methods=["GET", "POST"])
        ])


if __name__ == "__main__":
    app = MyApp()
    app.run("127.0.0.1", 80, debug=True)
