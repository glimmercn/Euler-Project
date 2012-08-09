'''
Created on 2011-7-30

@author: huangkan
'''

p=[1,1]
mil=10**6
n=1
while True:
    k=1
    n+=1
    sum=0
    while k*(3*k-1)//2<=n:
        if k%2==1: sum+=p[n-k*(3*k-1)//2]
        else:sum-=p[n-k*(3*k-1)//2]
        if k>0:k=-k
        else:k=-k+1
    if sum%mil==0:break
    p.append(sum%mil)
print(n)
         
             
       
    

    
