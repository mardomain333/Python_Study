n=int(input("enter the number"))
def fib(n):
    if n==1 or n==0:
        return n
    return fib(n-1)+fib(n-2)
  
print(fib(n))

count=0
l=1
r=1
while(count<n):
    print(l,end=" ")
    temp=r
    r=r+l
    l=temp
    count+=1
