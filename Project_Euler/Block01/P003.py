# Problem 003
# Largest prime factor

import math


def prime_factors(a):
    factors = []
    while a % 2 == 0:
        factors.append(int(2))
        a = a/2
    for i in range(3, int(math.sqrt(a))+1, 2):
        while a % i == 0:
            factors.append(int(i))
            a = a / i
    if a > 2:
        factors.append(int(a))
    return factors


print(max(prime_factors(600851475143)))
