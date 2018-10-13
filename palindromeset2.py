n=int(input())
def rev(n,temp):
    if(n==0):
        return temp
    temp=temp*10+(n%10)
    return rev(n//10,temp)
t=rev(n,0)
if(t==n):
    print("yes")
else:
    print("no")
    
