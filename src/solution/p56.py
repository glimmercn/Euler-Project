'''
Created on 2011-7-7

@author: huangkan
'''
max=0
for i in range(50,100):
    for j in range(30,100):
        li=list(str(i**j))
        sum=0
        for k in li:
            sum+=int(k)
        if sum>max:max=sum
print(max)
                