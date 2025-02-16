# Problem 002:
# Even Fibonacci Numbers

fib = [1, 2]

while (fib[-1] < 4_000_000):
    fib.append(fib[-1] + fib[-2])

sum = 0
for x in fib:
    if (x % 2 == 0):
        sum += x

print(sum)
