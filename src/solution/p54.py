'''
Created on 2011-7-6

@author: huangkan
'''
from Mytools import classification
    
def first(p): return [carddic[i[0]] for i in p]
def second(p):return [i[1] for i in p]
def straight(p):
    f=sorted(first(p))
    f=[i-f[0] for i in f]
    if f==list(range(5)):return 1
    else:return 0
def flush(p):
    s=second(p)
    if len(classification(s).keys())==1:return 1
    else:return 0
        
'''def RF(p):
    if sorted(first(p))[0]==10:return [flush(p)*straight(p)]
    else:return [0]'''
def SF(p):
    return [flush(p)*straight(p)*max(first(p))]
def Four(p):
    f=first(p)
    c=classification(f)
    if max(c.values())==4: 
        for i in c.keys():
            if c[i]==4:t=i
            else: tt=i
        return [t,tt]
    else:return [0,0]
def Fhouse(p):
    f=first(p)
    c=classification(f)
    if sorted(c.values())==[2,3]:
        for i in c.keys():
            if c[i]==3:x=i
            else:y=i
        return [x,y]
    else:return [0,0]
def Flush(p):
    return [flush(p)]
def Straight(p):
    return [straight(p)]
def Three(p):
    f=first(p)
    c=classification(f)
    if sorted(c.values())==[1,1,3]:
        for i in c.keys():
            if c[i]==3:t=i
        del c[i]
        x,y=sorted(c.keys())
        return [t,y,x]
    else:return [0,0,0]
def TwoPairs(p):
    f=first(p)
    c=classification(f)
    if sorted(classification(f).values())==[1,2,2]:
        t=[]
        for i in c.keys():
            if c[i]==2:t.append(i)
        x,y=sorted(t)
        del c[x]
        del c[y]
        z=list(c.keys())
        return [y,x]+z
    
    else:return [0,0,0]
def OnePair(p):
    f=first(p)
    c=classification(f)
    if sorted(c.values())==[1,1,1,2]:
        for i in c.keys():
            if c[i]==2:
                t=i
                break
        del c[t]
        z=sorted(c.keys())
        z.reverse()
        return [t]+z
    else:return [0]*4
def HCard(p):
    f=sorted(first(p))
    f.reverse()
    return f  
persons=[0]*5

carddic={}
for i in range(10):
    carddic[str(i)]=i
carddic['T']=10
carddic['J']=11
carddic['Q']=12
carddic['K']=13
carddic['A']=14
count=0
for i in open('poker.txt'):
    c=i.rstrip().split(' ')
    persons[0]=c[:5]
    persons[1]=c[5:]
    score=[0]*2
    for i in range(2):
        p=persons[i]
        score[i]=SF(p)+Four(p)+Fhouse(p)+Flush(p)+Straight(p)+Three(p)+TwoPairs(p)+OnePair(p)+HCard(p)
    i=0
    while score[0][i]==score[1][i]:i+=1
    if score[0][i]>score[1][i]:
        print('winner is 1')
        count+=1
    else:print('winner is 2')
print(count)
    
        
