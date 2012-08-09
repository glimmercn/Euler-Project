'''
Created on 2011-6-28

@author: huangkan
'''
import math
import time
max=0
con=set('123456789')
start=time.clock()
for i in range(2,9):
    for j in range(1,int(math.pow(10,math.floor(9/i)+1))):
        s=''
        for k in range(i):
            s+=str(j*(k+1))
        if len(s)==9 and set(s)==con and int(s)>max:
            print(s)
            max=eval(s)
elapsed=time.clock()-start
print(elapsed)
print(max)          
            