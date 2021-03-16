from json import dump
from itertools import zip_longest

with open("users.csv", "r") as users:
    with open("hobby.csv", "r") as hobby:

        all_list = zip_longest(("".join(us.split(",")) for us in users), hobby, fillvalue=None)
        my_dict = {str(el[0]).strip(): (el[1].strip()) for el in all_list}

        with open("ls.json", "w") as f:
            if "None" not in my_dict:
                dump(my_dict, f, ensure_ascii=False, indent=4)
                print(my_dict)
            else:
                exit(1)
