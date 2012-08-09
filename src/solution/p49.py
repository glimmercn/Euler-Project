'''
Created on 2011-7-4

@author: huangkan
'''
from Mytools import Isprime
import time
start=time.clock()
d={}
for i in range(1000,10000):
    if Isprime(i):
        s=str(sorted(list(str(i))))
        if s in list(d.keys()):
            d[s].append(i)
        else:
            d[s]=[i]
found=False
for i in d.keys():
    if len(d[i])>2:
        for j in range(1,len(d[i])):
            for l in range(j):
                if (d[i][l]+d[i][j])//2 in d[i]:
                    print(d[i][l],d[i][j],(d[i][l]+d[i][j])//2)
                    found=True
                    break
            if found:break
        if found:break
print(time.clock()-start)            
    