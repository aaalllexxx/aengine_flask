import os
import shutil
import json
from git import Repo


def main(base_dir, args):
    if args.get("-n"):
        with open(base_dir + "/env.json") as file:
            js = json.loads(file.read())

        js["project_folder"] = os.getcwd()
        js["project_name"] = args["-n"]

        with open(base_dir + "/env.json", "w") as file:
            file.write(json.dumps(js, indent=4))

        os.mkdir(args["-n"])
        os.mkdir(f'{args["-n"]}/screens')
        os.mkdir(f'{args["-n"]}/templates')
        os.mkdir(f'{args["-n"]}/static')
        shutil.copy(base_dir + "/templates/init/screens/HomeScreen.py", f'{args["-n"]}/screens')
        shutil.copy(base_dir + "/templates/init/config.json", f'{args["-n"]}')
        shutil.copy(base_dir + "/templates/init/main.py", f'{args["-n"]}')
        shutil.copy(base_dir + "/templates/init/templates/index.html", f'{args["-n"]}/templates')
        Repo.clone_from("https://github.com/aaalllexxx/aengine_flask", f"{args['-n']}/aengine_flask")

    else:
        print("Следует использовать флаг '-n' для указания имени проекта")