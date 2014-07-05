#!/usr/bin/python

import math

def isPrime(n):
    if (n % 2 == 0 and n != 2) or n <= 1:
        return False

    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

i = 0
primes = []
while len(primes) != 10001:
    if i < 3:
        i += 1
    else:
        i += 2
    if isPrime(i):
        primes.append(i)

print primes[-1:]
