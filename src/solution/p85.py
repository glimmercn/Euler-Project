'''
Created on 2011-8-5

@author: huangkan
'''
import math
a=1
ob=2*10**6
min=ob
while True:
    t=ob/(a+1)/a*4
    b=math.floor((t+.25)**.5-.5)
    if abs(ob-a*(a+1)*b*(b+1)//4)<min:
        ans=(a,b)
        min=abs(ob-a*(a+1)*b*(b+1)//4)
    b=math.ceil((t+.25)**.5-.5)
    if abs(ob-a*(a+1)*b*(b+1)//4)<min:
        ans=(a,b)
        min=abs(ob-a*(a+1)*b*(b+1)//4)
    if b<a:break
    a+=1
print(ans[1]*ans[0])
print(ans)
    