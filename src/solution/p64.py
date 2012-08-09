'''
Created on 2011-7-14

@author: huangkan
'''
from Mytools import continued_fractions
odd=0
for i in range(2,10001):
    if continued_fractions(i) is not None:
        if len(continued_fractions(i))%2==1:
            odd+=1
print(odd)
    