#!/usr/bin/python

import math

sum = 0

def isPrime(n):
    if (n % 2 == 0 and n != 2) or n <= 1:
        return False

    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

i = 0
primes = []
while i < 2000000:
    if i < 3:
        i += 1
    else:
        i += 2
    if isPrime(i):
        primes.append(i)

for j in primes:
    sum = sum+j

print sum

