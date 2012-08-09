'''
Created on 2011-6-6

@author: huangkan
'''
import math
sum=0
for n in range(23,101):
    f=1
    r=1
    while r<n:
         f*=(n-r+1)/(r)
         if f>1000000:break
         r+=1
    else:
        r=0
    if r:
        sum+=n-2*r+1
print(sum)
         