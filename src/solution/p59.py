'''
Created on 2011-7-9

@author: huangkan
'''
def timeof(word,li):
    count=0
    for i in range(len(li)-len(word)+1):
        for j in range(len(word)):
            if word[j]!=li[i+j]:break
        else:
            count+=1
    return count
de=open('cipher1.txt').read().split(',')
r=range(ord('a'),ord('z')+1)
de[len(de)-1]=de[len(de)-1][:-1]
de=[int(i) for i in de]
for i in r:
    for j in r:
        for k in r:
            key=i,j,k
            ans=[chr(de[i]^key[i%3]) for i in range(len(de))]
            if timeof('the',ans)>5:
                print(key)
                print(ans)
                print(sum([ord(i) for i in ans]))
                s=''
                for l in ans:s+=l
                print(s)
                
                

