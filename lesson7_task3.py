import os
from shutil import copytree
def copy():
    mp = "my project"
    tmpl = "templates"

    for root, dirs, files in os.walk(mp):
        if root.find(tmpl) >= 0 and len(files) == 0:
            copytree(os.path.join(root), tmpl, dirs_exist_ok=True)


if __name__ == "__main__":
    copy()
