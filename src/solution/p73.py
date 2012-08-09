'''
Created on 2011-7-29

@author: huangkan
'''
import math
from fractions import gcd
sum=0
for b in range(2,12000+1):
    for a in range(math.floor(b/3)+1,math.ceil(b/2)):
        if gcd(a,b)==1:sum+=1
print(sum)
    