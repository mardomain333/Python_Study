
import time
from math import sqrt
"""
Docstring for factoreof_numbers
  Here this pgm for find the factors for a number in 3 ways
  and i will show how these approaches the time complexity
"""



"""
1. first approach is brute force we will set a loop that starts from 1 to that 
number.and check whether each loop value is factore if factor then append to a result 
list
"""
def first_method(n):
    start=time.time()
    first_result=[]
    for i in range(1,n+1):
        if n%i==0:
            first_result.append(i)
    end=time.time()
    print("first_result",first_result)
    print("Time taken =",end-start)

"""

2.brute force optimal
by watching factors of some number we can see that the factors are number who cames 
before the half of the number like factor(10)
1,2,5,and 10 .for we can only run the loop to the half the number and append that number too
"""
def second_method(n):
    start=time.time()
    second_result=[]
    for i in range(1,n//+1):
        if n%i==0:
            second_result.append(i)
    second_result.append(n)
    end=time.time()
    print("second_result",second_result)
    print("Time taken =",end-start)

"""
3.using optimatal solution 
look at the example 36 .factor of 36
     1 - 36
     2 - 18
     3 - 12
     4 - 9
     6 - 6

 so we can see that we can see that we only want to run the loop root(n)
 time
"""
def third_method(n):
    start=time.time()
    third_result=[]
    root=int(sqrt(n))
    for i in range(1,root+1):
        if n%i==0:
            if n//i != i:
                third_result.append(i)
                third_result.append(n//i)
            else:
                third_result.append(i)
    third_result.sort()
    end=time.time()
    print("third_result",third_result)
    print("Time taken =",end-start)


n=int(input("Enter the number"))
choice=int(input("Enter the method 1,2,3 or 0>all"))
match choice:
    case 1:
        first_method(n)
    case 2:
        second_method(n)
    case 3:
        third_method(n)
    case 0:
        first_method(n)
        second_method(n)
        third_method(n)
