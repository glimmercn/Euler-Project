'''
Created on 2011-6-6

@author: huangkan
'''
from fractions import Fraction
x=Fraction(1,2)+Fraction(1)
d=len(str(x.denominator))
n=len(str(x.numerator))
fn=0
for i in range(1000):
    x=Fraction(1)+Fraction(1)/(x+Fraction(1))
    d=len(str(x.denominator))
    n=len(str(x.numerator))
    if n>d:fn+=1
print(fn)