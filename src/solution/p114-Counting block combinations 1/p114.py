'''
Created on Jan 23, 2013

@author: kan
'''
def num(n):
    numbers = [1]
    for i in range(1, n+1):
        a = i>2 and 1 or 0
        a += numbers[i-1]
        j = 4
        while not j>i:
            a += numbers[i-j]
            j += 1
        numbers.append(a)
    print(numbers)
    return numbers[n]

print(num(50))
        