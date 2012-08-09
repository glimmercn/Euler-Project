'''
Created on 2011-7-31

@author: huangkan
'''
import math
import Mytools

sum=0
print(int(Mytools.mysqrt(2*10**200)))
for i in range(2,100):
    if i**.5!=int(i**.5):
        t=int(math.sqrt(i*10**200))
        #print(len(str(t)))
        ints=list(str(t))
        for j in ints[1:]:
            sum+=int(j)
print(sum)