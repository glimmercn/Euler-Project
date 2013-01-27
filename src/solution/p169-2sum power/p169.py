'''
Created on Jan 25, 2013

@author: kan
'''


def f(n):
    '''f(n) is wrong'''

    if n < 2 :
        return 1
    else:
        if n % 2 == 1:
            return f(n-1)
        else:
            sum = 0
            for i in range(n//2+1):
                sum += f(i)
            return sum
        
def count(l):
    if len(l) == 1:
        if l[0] == 3:
            return 0
        else:
            return 1
    else:
        if l[0] == 0:
            return count(l[1:])
        if l[0] == 1 or l[0] == 2:
            l1 = l[1:]
            l2 = l[1:]
            l2[0] += 2
            return count(l1) + count(l2)
        if l[0] == 3:
            l1 = l[1:]
            l1[0] += 2
            return count(l1) 

def binarylist(n):
    s = str(bin(n))
    s1 = s[2:]
    l = list(s1)
    return [int(i) for i in l]

def count2(n):
    if n < len(ne):
        return ne[n]
    if n%2 == 0 :
        return count2(n//2) + count2(n//2-1)
    else:
        return count2(n//2)

ne = [1, 1, 2]
for i in range(3, 10000001):
    if i%2 == 0:
        ne.append(ne[i//2] + ne[i//2-1])
    else:
        ne.append(ne[i//2])

#print(ne)


print(count2(10**25))
            
    
        

