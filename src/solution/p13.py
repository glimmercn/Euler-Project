'''
Created on 2011-6-26

@author: huangkan
'''
input=open('data_p12.txt','r')
number=0
TenMillion=1e11
for line in input:    
    number+=int(line)

print(str(number)[0:10])
