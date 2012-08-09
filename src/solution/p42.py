'''
Created on 2011-7-3

@author: huangkan
'''
from Mytools import Is_tri_num
def word2num(w):
    sum=0
    for i in w:
        sum+=ord(i)-ord('A')+1
    return sum
counter=0
ifile=open('words.txt')
f=ifile.read()
l=list(f.split('","'))
l[0]=l[0][1:]
l[len(l)-1]=l[len(l)-1][:-1]
nums=list(map(word2num,l))
for i in nums:
    if Is_tri_num(i): counter+=1
print(counter)
