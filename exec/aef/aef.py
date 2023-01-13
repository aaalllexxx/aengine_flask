import os
import sys
from importlib import import_module


base_dir = os.sep.join(__file__.split(os.sep)[:-1])
modules = os.listdir(base_dir + os.sep + "modules")
commands = [i.strip(".py") for i in modules]

try:
    command = sys.argv[1]

    args = sys.argv[1:]
    args = dict(zip(args[1::2], args[2::2]))
    if command in list(commands):
        import_module("modules." + command).main(base_dir, args)

    else:
        print(f"Неизвестная команда: '{command}' пропишите '-h', чтобы просмотреть список комманд.")
except IndexError:
    print("Указаны некорректные аргументы. Пропишите '-h', чтобы просмотреть список комманд.")
