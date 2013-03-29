'''
Created on 2013-3-29

@author: kan
'''
import src.solution.Mytools as Mt
i = 1
p = 3 * i * i + 3 * i + 1
count = 0
while p < 1000000:
    count += Mt.Isprime(p)
    i += 1
    p = 3 * i * i + 3 * i + 1
print(count)