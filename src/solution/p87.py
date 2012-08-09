'''
Created on 2011-8-7

@author: huangkan
'''
limit=50*10**6
flag=[False]*(limit+1)
import Mytools
ps=Mytools.primes(int(limit**.5)+1)
for i in ps:
    sum=i*i
    for j in ps:
        sum=i*i+j*j*j
        if sum>limit:
            break
        else:
            for k in ps:
                sum=i**2+j**3+k**4
                if sum>limit:break
                else: flag[sum]=True
ans=0
for i in flag:
    if i:ans+=1
print(ans)