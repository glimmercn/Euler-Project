'''
Created on 2011-6-27

@author: huangkan
'''
def word_of_number(i):
    sum=''
    if i>99:        
        sum+=D[int(i/100)]+'hundred'
        i%=100
        if i>0:sum+='and'
                
    if i>19: 
        sum+=D[int(i/10)*10]
        i%=10
    sum+=D[i]
    return sum
D={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
   11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
   18:'eighteen',19:'nineteen',
   20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
sum=0
print(word_of_number(100))
for i in range(1,1000):
    sum+=len(word_of_number(i))
sum+=11
print(sum)
