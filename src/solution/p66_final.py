'''
Created on 2011-7-13

@author: huangkan
'''
import pell
max=3
ans=2
for i in range(3,1001):
    
    if i**.5!=int(i**.5):
        
        
        t,t2=pell.pell(i)
        if t>max:
            max=t
            ans=i
print(ans)