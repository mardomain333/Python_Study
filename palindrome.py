#this pgm show different ways to implement palindrome(simply kazhap :>)
#traditional loop method
string=input("enter the string")
l=0
r=len(string)-1
flag=0
while(l<r):
    if string[l]!=string[r]:
          flag=1
    l+=1
    r-=1
if flag==0:
     print(f"{string} is palindrome")
else:
     print(f"{string} is not palindrome")


#using python string slicing 
if string ==string[::-1]:
     print(f"{string} is palindrome")
else :
     print(f"{string} is not palindrome")

#using recursion

def is_pali(string,l,r):
     if l>r:
          return True
     elif string[l]!=string[r]:
          return False
     return is_pali(string,l+1,r-1)

if is_pali(string,0,len(string)-1):
     print(f"{string} is palindrome")
else :
     print(f"{string} is not palindrome")