'''
Created on 2011-5-1

@author: huangkan
'''

Boundary=1000000
f=open('primes.txt','r')
primes=[]
for line in f:
    primes.append(int(line))
f.close()
psum=[2]
PN=len(primes)
for i in range(1,len(primes)):
    psum.append(psum[i-1]+primes[i])
longest=0
i=1
while psum[i]<Boundary:
    if psum[i] in primes: 
        longest=i+1
        ans=psum[i]
    i+=2

i=1

while i+longest+1<PN:
    j=i+longest+1
    if (j-i)%2==0: j+=1
    while j<PN and psum[j]-psum[i]<Boundary:
        if (psum[j]-psum[i]) in primes:
            longest=j-i
            ans=psum[j]-psum[i]
            
        j+=2
    i+=1
print(ans)