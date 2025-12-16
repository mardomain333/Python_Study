"""
1                1

1 2            2 1

1 2 3        3 2 1

1 2 3 4    4 3 2 1

1 2 3 4  5 4 3 2 1

done by myown logic
"""



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
  



"""

           1     
         1 2 1    
       1 2 3 2 1
     1 2 3 4 3 2 1
   1 2 3 4 5 4 3 2 1
   done by myown login proud :>>>
"""
n=int(input("Enter the number"))
n=n+1
for i in range(1,n):
        string=""
        count=0                   #this my idea for printing the space before the number if i=1 that means (n-1) (5-1) 4 spaces
                                   #are requried
        string+="  "*(n-i)
        m=i+(i-1)


        for j in range(1,m+1):
                if j<=(m//2)+1:
                        count+=1
                        string+=" "+str(count)       #this is the logic for printing the number pattern
                        
                else:
                        count-=1
                        string+=" "+str(count)
        
                
        string+="  "*(n-i)
        print(string)
                

