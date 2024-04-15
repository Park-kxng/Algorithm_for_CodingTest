import sys

def generate_primes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit+1, i):
                primes[j] = False
    return [x for x in range(limit+1) if primes[x]]

def isPal(number):
    temp = list(str(number))
    start = 0
    end = len(temp) - 1
    while start <= end:
        if temp[start] != temp[end]:
            return False
        start += 1
        end -= 1
    return True

input = sys.stdin.readline
n = int(input())

# Generate primes up to 1000000
primes = generate_primes(1000000)

# Find the smallest prime palindrome greater than or equal to n
for i in range(n, 1000001):
    if i in primes and isPal(i):
        print(i)
        break