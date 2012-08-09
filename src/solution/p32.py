'''
Created on 2011-6-27

@author: huangkan
'''
sum=set()
for i in range(1,10000):
    for j in range(i+1,10000):
        if (len(str(i))+len(str(j))+len(str(i*j)))>9:break
        else:
            if len(set(str(i)+str(j)+str(i*j))-{'0'})==9:
                print(i,'*',j,'=',i*j)
                sum.add(i*j)
s=0
print(sum)
for i in sum:
    s+=i
print(s)
                