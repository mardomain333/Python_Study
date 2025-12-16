n=5


max=2*n-1
for i in range(1,n+1):
    if i!=n:
        string=""
        for j in range(1,i+1):
            string+=str(j)
            string+=" "
        print(string,end="")
        for j in range(max-(i*2)):
            print(" ",end=" ")
        print(string[::-1])
        print()
    else:
        string=""
        for j in range(1,i):
            string+=str(j)
            string+=" "
        print(string,end=" ")
        print(n,end="")
        print(string[::-1])
  

