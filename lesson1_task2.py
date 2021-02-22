from typing import List, Any, Union

cub: list[Union[int, Any]] = []
sum = 0

for i in range(1, 1001, 2):
    cub.append(i ** 3)

for ind, val in enumerate(cub):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum += cub[ind]
    cub[ind] += 17
print(sum)

sum = 0

for ind, val in enumerate(cub):
    sum_digits = 0
    while val:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum += cub[ind]
