with open("nginx_logs.txt", "r") as a:
    ls = ([line.split()[0], line.split()[5], line.split()[6]] for line in a)
    for b in ls:
        print(b)