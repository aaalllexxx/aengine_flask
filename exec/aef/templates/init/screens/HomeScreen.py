from screen import Screen
from flask import render_template


class HomeScreen(Screen):
    def main(self):
        return render_template("index.html")
