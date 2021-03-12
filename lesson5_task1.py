def odd_nums(num):
    for nums in range(1, num + 1, 2):
        yield nums

for i in odd_nums(15):
     print(i)
