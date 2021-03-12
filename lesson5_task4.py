ls = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ls_line = [ls[nums] for nums in range(1, len(ls)) if ls[nums] > ls[nums -1]]
print(ls_line)
