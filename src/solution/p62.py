'''
Created on 2011-7-11

@author: huangkan
'''
d={}
length=1
found=False
i=100
length=len(str(i**3))
while not found:
    i+=1
    if len(str(i**3))==length:
        li=sorted(list(str(i**3)))
        if str(li) in d.keys():
            d[str(li)][1]+=1
        else:
            d[str(li)]=[i,1]
    else:
        for j in d.keys():
            if d[j][1]==5:
                found=True
                print(d[j][0])
        d={}
        if not found:
            li=sorted(list(str(i**3)))
            d[str(li)]=[i,1]
            length=len(str(i**3))
