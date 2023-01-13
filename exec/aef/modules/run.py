import json
import os
import platform


def main(base_dir, args):
    with open(base_dir + "/env.json") as file:
        js = json.loads(file.read())

    project_folder = js["project_folder"]
    project_name = js["project_name"]
    if platform.system().lower() == "windows":
        command = f"python {os.path.join(project_folder, project_name, 'main.py')}"
        os.system(command)
