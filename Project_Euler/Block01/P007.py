# 10 001s Prime
import math
from itertools import count

primeNumbers = [2]


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


def is_prime(x):
    return len(prime_factors(x)) == 1


for x in count(3, 2):
    if is_prime(x):
        primeNumbers.append(x)
        print(f"Adding: {x}")
    if (len(primeNumbers) == 10_001):
        print(primeNumbers[-1])
        break
