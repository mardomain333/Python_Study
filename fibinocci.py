#recursion
n=int(input("enter the number"))
def fib(n):
    if n==1 or n==0:
        return n
    return fib(n-1)+fib(n-2)
  
print(fib(n))

#tradional
count=0
l=1
r=1
while(count<n):
    print(l,end=" ")
    temp=r
    r=r+l
    l=temp
    count+=1
print()

#dynamic programing

dp=[1,1]
for i in range(2,n):
    dp.append(dp[i-1]+dp[i-2])
print(dp)
