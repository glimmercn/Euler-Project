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
    if li[0]<2000:
        if len(li)<2:
            li.append(li[-1]+1)
            search(li)
        else:
            if sum([p[i] for i in li])>=min:
                li.pop()
                li[-1]+=1
                search(li)
            else:                   
                plist=[p[i] for i in li]
                last=li[-1]
                for j in li[:-1]:                
                    if not Mytools.Isprime(cont(p[last],p[j])) or not Mytools.Isprime(cont(p[j],p[last])):
                        li[-1]+=1
                        search(li)
                        break
                else:               
                    if len(li)==5:                
                        min=sum(li)
                        print(plist)
                        li[-1]+=1
                        search(li)
                    else:
                        li.append(li[-1]+1)
                        search(li)
                        

limit=27000
min=30000
pr=Mytools.primes_shelter(limit)
p1=[i for i in range(limit) if pr[i] and i%3==1]
p2=[i for i in range(limit) if pr[i] and i%3==2]
p=[3]+p1
Oracle=Mytools.PrimeOracle()
search([0])
        
           
 
                    
    