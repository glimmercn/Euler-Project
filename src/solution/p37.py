'''
Created on 2011-6-28

@author: huangkan
'''
def tp(i):
    s=str(i)
    for j in range(1,len(s)):
        if eval(s[:j]) not in prime:
            return False
    for j in range(1,len(s)):
        if eval(s[j:]) not in prime:
            return False
    return True
            
import solution.Mytools
prime=solution.Mytools.primes2(1000000)

print(tp(15))   
sum=0
counter=0
for i in prime:
    if i>7:
        if tp(i):
            sum+=i
            counter+=1
            print(i)
        if counter==11:break
print(counter)
print(sum)
