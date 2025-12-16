
"""
Docstring for recursion_study02

ith recursion nte second part an ithil parameterised and functional
recursion ne kurich an nammal samsarikune
"""
##parameterised recursion 
#just write a pgm to find the sum of n numbers

def find_sum(i,n,sum):
    if i>n:
        print(f"sum using parameterised={sum}")
        return                      #yi function parameter pass cheytha ann work 
                                    #cheyune ini return cheyth olle pgm kanam

    find_sum(i+1,n,sum+i)

find_sum(1,5,0)

def find_sum(n):
    if n==1:
        return 1                                #ivide backtracking cheyanne return cheyth
    else:
        return n+find_sum(n-1)
print(f"sum using functional={find_sum(5)}")


"""
yi concept thanne namuk factorial implement cheyam use akkam
"""
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number to find factorial::"))
print(f"factorial of {n}= {fact(n)}")



"""
now i going to just reverse a list using recursion

"""
arr=[1,2,3,4,5]
def reverse(arr,l,r):
    if r<l:
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverse(arr,l+1,r-1)
reverse(arr,0,len(arr)-1)
print(arr)

