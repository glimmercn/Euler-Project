'''
Created on 2011-7-3

@author: huangkan
'''
def list2str(li):
    s=''
    for i in li:
        s+=i
    return s

from Mytools import all_perms
sum=0
prime=[2,3,5,7,11,13,17]
for p in all_perms(list('0123456789')):
    for i in range(7):
        if int(list2str(p[i+1:i+4]))%prime[i]!=0 :
               break
    else:
        sum+=int(list2str(p))
print(sum)