'''
Created on 2011-7-3

@author: huangkan
'''
def samednum(i):
    return int(10**(i-1)*9)
l=0
#digits in one number
nd=0
ans=1
li=[]

for i in [10,100,1000,10000,100000,1000000]:
    while l+samednum(nd+1)*(nd+1)<i:
        l+=samednum(nd+1)*(nd+1)
        nd+=1
    res=i-l
    a=res//(nd+1)
    '''
    print(10**nd+a)
    print()
    '''
    p=str(10**nd+a-1)[-1:] if res%(nd+1)==0 else str(10**nd+a)[res%(nd+1)-1]
    print(p)
    ans*=int(p)
print(ans)