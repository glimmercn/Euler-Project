'''
Created on 2011-7-9

@author: huangkan
'''
def cont(i,j):
    return int(str(i)+str(j))
#from Mytools import primes
from Mytools import Isprime
import Mytools
from itertools import combinations
estimate=1000000
limit=100000
pr=Mytools.primes_shelter(limit)
p1=[i for i in range(limit) if pr[i] and i%3==1 and i>673]
t=[3,7,109,673]
Oracle=Mytools.PrimeOracle()
i=673
while True:
    if Mytools.Isprime(i):
    
        for j in t:
            
            if not Mytools.Isprime(cont(i,j)) or not Mytools.Isprime(cont(j,i)):
                break
        else:
            print(i)
            break
    i+=6

    
