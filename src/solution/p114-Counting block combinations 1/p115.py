'''
Created on Jan 23, 2013

@author: kan
'''
def num(n, m):
    numbers = [1]
    for i in range(1, n+1):
        a = i>m-1 and 1 or 0
        a += numbers[i-1]
        j = m+1
        while not j>i:
            a += numbers[i-j]
            j += 1
        numbers.append(a)
#    print(numbers)
    return numbers

i = 50
block = num(200, 50)
while i<len(block) and block[i]<1000000 :
    i += 1
print(i)
        