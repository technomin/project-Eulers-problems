#!/usr/bin/python
sumsq = 0

for i in range(1, 101):
    sumsq += i ** 2

sqsum = (sum(range(1, 101))) ** 2

dif = sqsum - sumsq
print dif