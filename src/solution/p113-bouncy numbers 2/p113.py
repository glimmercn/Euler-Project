'''
Created on Jan 2, 2013

@author: kan
'''
def bio(n, k):
    if k > n:
        return 1
    else:
        m = n-k > k and k or n-k
        com = 1
        for i in range(n-m+1, n+1):
            com *= i
        for i in range(1, m+1):
            com /= i
        return com
    
def notbouncy(n):
    ans = bio(n+9, 9) * 2 - 2
    for i in range(1, n):
        ans += bio(i+9, 9) - 1
    ans -= n*9
    return ans
print(notbouncy(100))

