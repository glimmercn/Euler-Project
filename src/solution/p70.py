'''
Created on 2011-7-15

@author: huangkan

I delete the right edition mistakenly. This code is to slow to get the answer.
The key point is to measure the rate and length of totient whenever a new factor is found. It will accelerate the whole search.
'''

from Mytools import primes
p=primes(3163)
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
min=10**7
ans=1

for i in range(3,int(10**7)):
    r=int(Totient(i))
    il=sorted([int(j) for j in list(str(i))])
    rl=sorted([int(j) for j in list(str(r))])
    if il==rl:
        rate=i/r    
        if rate<min:
            min=rate
            ans=i
print(ans)