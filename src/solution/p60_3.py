'''
Created on 2011-7-10

@author: huangkan
'''
def cont(i,j):
    return int(str(i)+str(j))
#from Mytools import primes

import Mytools

def search(li):
    global min
    if li==[]:
        for i in range(0,len(p)-4):
            li.append(i)
            search(li)
            li.pop()
    else:
        if len(li)<2:
            for i in range(li[-1]+1,len(p)):
                li.append(i)
                search(li)
                li.pop()
        else:
            if sum([p[i] for i in li])<min:                   
                plist=[p[i] for i in li]
                last=li[-1]
                for j in li[:-1]:                
                    if not Mytools.Isprime(cont(p[last],p[j])) or not Mytools.Isprime(cont(p[j],p[last])):
                        break
                else:               
                    if len(li)==5:                
                        min=sum(li)
                        print(plist)
                    else:
                        for i in range(li[-1]+1,len(p)):
                            li.append(i)
                            search(li)
                            li.pop()
                        

limit=27000
min=30000
pr=Mytools.primes_shelter(limit)
p1=[i for i in range(limit) if pr[i] and i%3==1]
p2=[i for i in range(limit) if pr[i] and i%3==2]
p=[3]+p1
Oracle=Mytools.PrimeOracle()
search([])
        
           
 
                    
    