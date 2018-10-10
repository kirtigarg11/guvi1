n=(input())
s='bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
if(n in ('a','e','i','o','u','A','E','I','O','U')):
   print("Vowel")
elif(n in s):
   print("Consonant")
else:
    print("Invalid")
    
   
