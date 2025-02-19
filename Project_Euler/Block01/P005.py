# Smallest multiple
import math

smallest = 1
current_divisor = 1
primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]
biggest_divisor = 20


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


while current_divisor <= biggest_divisor:
    if smallest % current_divisor == 0:
        # number = number * lastDivisor
        ...
    elif current_divisor in primeNumbers:
        smallest = smallest * current_divisor
    else:
        currentPrimeFactors = prime_factors(current_divisor)
        for x in currentPrimeFactors:
            smallest = smallest * x
            if smallest % current_divisor == 0:
                break
    # Increment the divisor by 1
    current_divisor += 1

print(smallest)
