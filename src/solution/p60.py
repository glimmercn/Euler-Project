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
limit=26000
pr=Mytools.primes_shelter(limit)
p1=[i for i in range(limit) if pr[i] and i%3!=2]
p2=[i for i in range(limit) if pr[i] and i%3!=1]
Oracle=Mytools.PrimeOracle()
for i in combinations(p1,5):
    if sum(i)<793:continue
    for j in combinations(i,2):
        if not Oracle.isprime[cont(j[0],j[1])] or not Oracle.isprime[cont(j[1],j[0])]:
            
            break
    else:
        if sum(i)<estimate:
            estimate=sum(i)
            print(estimate)
            print('the primes are',i)
print(estimate)
    
