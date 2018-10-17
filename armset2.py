n=input()
order=len(n)
su=0
temp=0
n=int(n)
k=n
while(n!=0):
   temp=n%10
   n=n//10
   su=su+temp**order
if(su==k):
    print("yes")
else:
    print("no")

