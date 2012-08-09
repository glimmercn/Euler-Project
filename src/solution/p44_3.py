'''
Created on 2011-7-4

@author: huangkan
'''
Limit=100000000
def Ispenta(i):
    if i<Limit:
        return i in f
    else:
        a=int((1+(1+24*i)**.5)/6)
        b=a+1
        if penta(a)==i or penta(b)==i: return True
        else:
            return False
def penta(i):
    return (3*i-1)*i//2
f=[penta(i) for i in range(1,8166)]
j=1
found=False
print(Ispenta(penta(817)-2))

while not found:
    k=j+1
    while f[k]-f[j]<=f[j-1]:
        
        if Ispenta(f[k]-f[j]) and Ispenta(f[k]+f[j]):
            found=True
            print(f[k]-f[j])
            break
        if f[j]>Limit:
            found=True
            print("No answer")
            break
        k+=1
    j+=1
