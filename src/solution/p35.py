'''
Created on 2011-4-30

@author: huangkan
'''
from solution.Mytools import primes2
prime=primes2(1000000)
sum=0
for t in range(len(prime)):
    i=prime[t]
    Iscircular=True
    for j in range(1,len(str(i))):
        s=str(i)
        inew=int(s[j:]+s[:j])
        if not inew in prime:
            Iscircular=False
            break
        
    if Iscircular:
        sum+=1
print(sum)
