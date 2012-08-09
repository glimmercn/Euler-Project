'''
Created on 2011-6-29

@author: huangkan
'''
import math

max=0
max_p=0
for p in range(10,1000,2):
    counter=0
    for c in range(p//3+1,p//2+1):       
        sum=p-c
        product=(p*p-2*p*c)//2
        if sum*sum/4>product:
            a=int(sum/2+ math.sqrt(sum*sum/4-product))
            b=sum-a
            if a*a+b*b==c*c and a*b>0:counter+=1
            #print(a,b,c)
        if counter>max: 
            max=counter
            max_p=p
print(max_p)