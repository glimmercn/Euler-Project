'''
Created on 2011-8-5

@author: huangkan
'''
import math
max=1   
solution=0 
while True:
    max+=1
    for i in range(2,max*2+1):
        sum=i*i+max*max
        if math.sqrt(sum)==int(math.sqrt(sum)):
            if i<max+1:
                solution+=i//2
            else:
                solution+=(2*max-i)//2+1
    if solution>10**6:
        
        break
print(max)