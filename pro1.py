#!/usr/bin/python

def Sum():
    result = 0
    for i in range(2, 1000):
        if isMultiple(i):
            result += i 
    print(result)

def isMultiple(i):
    return (i % 3 == 0) or (i % 5 == 0)

Sum();