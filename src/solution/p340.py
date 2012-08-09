'''
Created on 2011-10-1

@author: huangkan
'''
import math
def f(n):
    if n>b: return n-c
    else: 
        return f(a+f(a+f(a+f(a+n))))
billion=10**9

a=21**7
b=7**21
c=12**7
k=math.floor(b/a)
ans=b*(b+1)/2+4*(a-c)*(b+1)+(4*a-3*c)*(a*k*(k-1)/2+k*((b+1)%a))
print(ans%10**9)
print('%f' %ans)
k=b//a
ans=b*(b+1)/2+4*(a-c)*(b+1)+(4*a-3*c)*(a*k*(k-1)/2+k*((b+1)%a))
print(ans%10**9)
print('%i' %ans)
