# Special Pythagorean triplet

from itertools import count
from math import sqrt

expected_sum = 1000

for a in count(1):
    sum = 0
    for b in count(a + 1):
        c = sqrt((a ** 2) + (b ** 2))
        sum = a + b + c
        if sum == expected_sum:
            print(a * b * c)
            break
        elif c > 500:
            break
    if sum == expected_sum:
        break
