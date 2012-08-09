'''
Created on 2011-10-1

@author: huangkan
'''
import Mytools
import math
l=50
ans=l*l*3
for x in range(1,l+1):
    for y in range(1,l+1):
        g=Mytools.gcd(x, y)
        x1=x/g
        y1=y/g
        k=min(math.floor((l-x)/y1),math.floor(y/x1))
        ans+=k*2
print(ans)
        