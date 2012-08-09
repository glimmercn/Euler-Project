'''
Created on 2011-7-29

@author: huangkan
'''
from Mytools import primes
p=primes(1000)
def factors(d):
    f=[]
    for i in p:
        if d>1 and d not in p:
            if d%i==0:
                f.append(i)
                while d%i==0:
                    d=d//i
        else:
            break
    if d>1:f.append(d)
    return f

def Totient(n):
    n1=n
    f=factors(n)
    
    for i in f:
        n1=n1*(i-1)//i
    return n1
sum=0
for i in range(2,1000000+1):
    sum+=Totient(i)
print(sum)