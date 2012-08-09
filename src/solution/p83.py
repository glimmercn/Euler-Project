'''
Created on 2011-8-3

@author: huangkan
'''
move=[(1,0),(-1,0),(0,1),(0,-1)]
mtx=[]
for i in open('matrix83.txt'):
    n=[int(j) for j in list(i.rstrip().split(','))]
    mtx.append(n)
outed=dict()
outed[(0,0)]=mtx[0][0]
while (79,79) not in outed.keys():
    min=10**10
    for i in outed.keys():
        for j in move:
            if -1<i[0]+j[0]<80 and -1<i[1]+j[1]<80 and (i[0]+j[0],i[1]+j[1]) not in outed.keys():
                if outed[i]+mtx[i[0]+j[0]][i[1]+j[1]]<min:
                    min=outed[i]+mtx[i[0]+j[0]][i[1]+j[1]]
                    cad=(i[0]+j[0],i[1]+j[1])
    outed[cad]=min
print(outed[(79,79)])

