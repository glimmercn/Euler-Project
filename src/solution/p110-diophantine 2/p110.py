'''
Created on Dec 29, 2012

@author: kan

'''
import math
def dio(fs):
    ans = 1;
    for i in fs:
        ans *= 2 * i + 1 
    return ans

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
lprimes = [math.log(i) for i in primes]
factors = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
fs = dio(factors)
found = False
therashold = 8000000-1
while not found:
    for i in range(len(primes)):
        if fs/(2 * factors[i] + 1) * (2 * factors[i] + 3) > therashold:
            found = True
            factors[i] += 1
            break
    if not found:    
        opt = 0;
        inc = fs/(2 * factors[0] + 1)/lprimes[0]
        
        i = 1
        while i < len(primes):
            if fs/(2 * factors[i] + 1)/lprimes[i] > inc:
                opt = i
                inc = fs/(2 * factors[i] + 1)/lprimes[i]
            i += 1
        factors[opt] += 1
        fs = dio(factors)
print(factors)

ans = 1 
for i in range(len(primes)):
    ans *= primes[i] ** factors[i]
print(ans)

obj = 9350130049860600
objf = []
for i in range(len(primes)):
    j = 0
    while obj % primes[i] == 0:
        j += 1
        obj /= primes[i]
    objf.append(j)
print(objf)