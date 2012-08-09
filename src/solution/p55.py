'''
Created on 2011-7-14

@author: huangkan
'''
'''
Created on 2011-7-6

@author: huangkan
'''
def val(n):
    s=''
    for i in n:
        s+=i
    return int(s)
count=0
for i in range(10000):
    num=list(str(i))
    r=num[:]
    r.reverse()
    num=list(str(val(num)+val(r)))
   
    for j in range(50):
        r=num[:]
        r.reverse()
        if num==r:break
        num=list(str(val(num)+val(r)))
    else:
        count+=1
print(count)
        
    
             
             
    