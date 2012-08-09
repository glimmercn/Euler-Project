'''
Created on 2011-10-2

@author: huangkan
'''

def f(n):
    if n==9999: return 11112222222222222222
    fn=n
    OK=False
    while not OK:
        strfn=str(fn)
        OK=True
        for i in xrange(len(strfn)):
            if not strfn[i] in ['0','1','2']:
                OK=False
                p=10**(len(strfn)-i-1)
                minfn=((fn//p)+1)*p
                fn=((minfn-1)//n+1)*n
                break
    return fn
            
def euler303(nmax):
    s=0
    for n in xrange(nmax):
        s+=f(n+1)//(n+1)
    return s

print f(9)
print f(99)
print f(999)
print euler303(100)
print euler303(10000)
'''def max2(l):
    return int('2'*l)
def min2(l):
    return 10**(l-1)
#this method is to get the minimum number which is greater than n and consists with 0, 1, 2.
def mingter(n):
    if len(n)>1:        
        if int(n[1:])>max2(len(n)-1):
            return str(int(n[0])+1)+'0'*(len(n)-1)
        else:
            return n[0]+mingter(n[1:])
    else:
        return str(int(n)+1)
#this function is to get the mininum multiply of n which is equal or greater than a.         
def mingtermulti(a,n):
    return ((a-1)//n+1)*n
def if2(n):
    for i in str(n):
        if int(i)>2:return False
    return True
def f(n):
    candidate=mingtermulti(c[n],n)
    while not if2(candidate):
        candidate=mingtermulti(int(mingter('0'+str(candidate))),n)
    return candidate
sum=0
limit=10000
c=[i for i in range(limit+1)]
for i in range(2,limit+1):
    c[i]=ans=f(i)
    for j in range(2,limit//i+1):
        if ans>c[i*j]:c[i*j]=ans
    sum+=ans//i
print(sum)        
'''   


