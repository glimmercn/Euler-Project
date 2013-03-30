'''
Created on Mar 29, 2013

@author: kan
'''
import src.solution.Mytools as Mt
primes = Mt.primes2(1000003)
def S(p1, p2):
    l = len(str(p2))
    dig = 10**l
    p = p2
    while p % dig != p1:
        p += p2
    return p

sum = 0
for i in range(2, len(primes)-1):
    sum += S(primes[i], primes[i+1])
print(sum)

