'''
Created on 2011-7-30

@author: huangkan
'''
import Mytools
limit=100
l=[0]*(limit+1)
for i in range(0,limit+1):
    if i%2==0:
        l[i]=1
p=Mytools.primes(limit)
for i in p[1:]:
    tl=l[:]
    for j in range(1,int(limit/i)+1):
        for k in range(limit+1):
            if k+i*j<limit:
                l[k+i*j]+=tl[k]
            else:
                break
print(l)
for i in range(limit):
    if l[i]>5000:
        print(i)
        break