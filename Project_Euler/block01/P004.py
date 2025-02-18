# Largest palindrome

def isPalindrome(number: int):
    return int(str(number)[::-1]) == number


palindromes = []

for x in range(1000, 900, -1):
    for y in range(1000, 900, -1):
        if isPalindrome(x * y):
            palindromes.append(x * y)

print(max(palindromes))
