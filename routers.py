from typing import Callable


class Router:
    def __init__(self, rules: str | list, view_func: Callable, **options):
        self.rules = rules
        self.view_func = view_func
        self.options = options

    def to_dict(self):
        return dict(rules=self.rules, view_func=self.view_func, **self.options)
