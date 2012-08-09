'''
Created on 2011-4-30

@author: huangkan
'''
f=[1]
t=1
sum=0
for i in range(1,10):
   t*=i
   f.append(t) 
for i in range(4,4000000):
    j=i
    fsum=0
    while j>0:
        fsum+=f[j%10]
        j=int(j/10)
    if fsum==i:sum+=i
    
print(sum)
        