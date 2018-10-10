import re
n=input()
p=re.compile('[a-zA-Z]')
s=re.search(p,n)
if(s!=None):
    print("Yes")
else:
    print("No")
