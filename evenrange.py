import math
i,j=map(int,input().split())
re=[]
for k in range(i+1,j+1):
    if(k%2==0):
        re.append(k)
print(*re,sep=" ")
