import re
x=0
count=0
hand= open('work.txt')
for i in hand:
    
    l=re.findall('[0-9]+',i)
    for j in l:
        h=int(j)
        x=x+h
        count=count+1
print("There are  "+str(count)+" numbers with sum of "+ str(x))