'''
Created on 2011-7-12

@author: huangkan
'''
from math import ceil
import math
from fractions import Fraction
def isinteger(x):
    error=.1**10
    if x-math.floor(x)<error or math.ceil(x)-x<error:
        return True
    else:
        return False
def integer(x):
    error=.1**10
    if x-math.floor(x)<error:return math.floor(x)
    if math.ceil(x)-x<error:return math.ceil(x)
def pellsolution(x):
    sroot=x**.5
    li=[]
    y=x**.5
    li.append(math.floor(y))
    y=1/(y-math.floor(y))
    while not isinteger(y-sroot):
        li.append(math.floor(y))
        y=1/(y-math.floor(y))
    li.append(integer(y-sroot))
    if len(li)%2==0:
        tli=li[1:]
        li[-1]+=li[0]
        li=li+tli
    li.pop()
    ans=Fraction(li[-1],1)
    
    for i in range(len(li)-2,-1,-1):
        ans=Fraction(li[i],1)+Fraction(1,1)/ans
    return ans.numerator
max=3
print(pellsolution(14))

for i in range(2,1001):
    if i**.5!=int(i**.5):
        a=pellsolution(i)
        if a>max:
            ans=i
            max=a         
print(ans)
