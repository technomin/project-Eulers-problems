#!/usr/bin/python

num = 600851475143

for i in range(2,num):
    if num%i == 0:
        isprime = true
        for j in range(2,i):
            if i%j == 0:
                isprime = false
                break

        if isPrime:
            lf = i

print "the largest prime factor is : ",lf