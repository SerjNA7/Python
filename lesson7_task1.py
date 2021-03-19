import os

ls = {"my project": ["settings", "mainapp", "adminapp", "authapp"]}


def mkdir(ls_p):
    for f, s in ls_p.items():
        if os.path.exists(f):
            continue
        i: int
        for i in range(len(s)):
            os.makedirs(os.path.join(f, s[i]))


mkdir(ls)
