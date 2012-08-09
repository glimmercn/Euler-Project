'''
Created on 2011-4-27

@author: huangkan
'''
from solution.Mytools import Isprime
def quadratic(a,b):
    return lambda n:n*n+a*n+b
longest=0
longest_a=0
longest_b=0
for a in range(-999,1000):
    for b in range(-999,1000):
        f=quadratic(a,b)
        accounter=0
        i=0
        while Isprime(f(i)):
            i=i+1
        if longest<i:
            longest=i
            longest_a=a
            longest_b=b
print(longest_a*longest_b)
        