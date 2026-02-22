"""
Docstring for python

int 
string
float
double
bool
range
list
tuple
set

"""
from functools import reduce

def decorator(func):
    def wrapper(x,y):
         if x<y:
              return func(y,x)
         else:
              return func(x,y)

    return wrapper
@decorator
def sub(x,y):
     print(x-y)


sub(9,7)
sub(7,9)


l=[1,2,3,4,5]
print(list(filter(lambda x:x&1,l)))
print(list(map(lambda x:x**2,l)))
print(reduce(lambda x,y:x+y,l))


group=[{"name":"gokul",
      "age":23,
      "mark":34}]


def happy(name,age,mark):
     print(f"hi {name} u are {age} years old u r mark{mark}")
happy(**group[0])