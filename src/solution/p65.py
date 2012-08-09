'''
Created on 2011-7-14

@author: huangkan
'''
from fractions import Fraction
from Mytools import contif2frac
e=[2]
for i in range(1,34):
    e.append(1)
    e.append(i*2)
    e.append(1)
print(len(e))

a=contif2frac(e)
print(sum([int(i)for i in list(str(a.numerator))]))