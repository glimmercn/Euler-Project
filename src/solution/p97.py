'''
Created on 2011-10-6

@author: huangkan
'''
import Mytools
ten10=10**10
l=list(Mytools.int2(7830457,2))

ans=1
for i in l:
    if i=='0':
        ans=ans*ans%ten10
    else:
        ans=ans*ans*2%ten10
ans=(ans*28433+1)%ten10
print(ans)
print(l)