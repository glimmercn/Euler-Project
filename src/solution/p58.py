'''
Created on 2011-7-7

@author: huangkan
'''
import time
from Mytools import Isprime
start=time.clock()
length=50001
limit=length**2

#primes=primes_shelter(limit)
num=1
d_count=1
p_count=0
for i in range(length//2):
    add=2*(i+1)
    for j in range(4):
        num+=add
        if Isprime(num): p_count+=1
    d_count+=4
    if p_count/d_count<.1:
        print(i*2+3)
        break
else:
    print('not big enough')
print(time.clock()-start,'seconds')
        