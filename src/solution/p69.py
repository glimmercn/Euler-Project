'''
Created on 2011-7-14

@author: huangkan
'''
from Mytools import primes
p=primes(1000)
def factors(d):
    f=[]
    for i in p:
        if i>1:
            if d%i==0:
                f.append(i)
                while d%i==0:
                    d=d//i
        else:
            break
    if d>1:f.append(i)
    return f

def Totient(n):
    n1=n
    f=factors(n)
    
    for i in f:
        n1*=(i-1)/i
    return n1
maximum=2
ans=2

for i in range(3,1000000):
    r=i/Totient(i)
    if r>maximum:
        maximum=r
        ans=i
print(ans)