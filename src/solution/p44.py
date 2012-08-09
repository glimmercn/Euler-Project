'''
Created on 2011-4-30

@author: huangkan
'''
import math
def penta(i):
    return int((3*i-1)*i/2)
def Ispentagon(x):
    a=int((1+math.sqrt(1+24*x))/6)
    b=a+1
    if penta(a)==x or penta(b)==x: return True
    return False
pentalist=[1,5]
found=False
i=3
while not found:
    temp=penta(i)
    pentalist.append(temp)
    for iter in range(len(pentalist)-1):
        if Ispentagon(pentalist[iter]+temp) and Ispentagon(pentalist[iter]+2*temp):
            found=True
            answer=pentalist[iter]
            break
    i+=1
print(answer)