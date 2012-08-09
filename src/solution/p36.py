'''
Created on 2011-6-28

@author: huangkan
'''
sum=0
for i in range(1,1000000,2):
    if str(i)==str(i)[::-1] :
        b='{0:b}'.format(i)
        if b==b[::-1]:
            sum+=i
print(sum)