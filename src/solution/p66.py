'''
Created on 2011-7-12

@author: huangkan
'''
max=3
ans=2
for i in range(3,1001):
    
    if i**.5!=int(i**.5):
        j=0
        while True:
            j+=1
            if int((1+i*j**2)**.5)==(1+i*j**2)**.5:
                break
        t=(1+i*j**2)**.5
        if t>max:
            max=t
            ans=i
print(ans)