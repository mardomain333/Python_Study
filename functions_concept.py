
"""
Docstring for functions_concept

function in python is actually a object which is stored in memory
the name of function is just a reference to that object
"""

def add(a,b):  # add is the name which reference to the function object 
                  # here a and b are parameters and 5,6 are arguments
    return a+b
print(add(5,6))

print(add)   #shows the add object memory address
print(type(add)) #show the add is an object of class <function>


"""
FUNCTIONS ARGUMENTS CAN BE OF DIFFERENT TYPES
    1.POSITIONAL 
    2.KEYWORD
    3.DEFAULT
"""
#POSITIONAL
def printer(a,b):
    print(a,b)
printer(4,5)         #order is important


#keyword(named arguement)

def printer(a,b):
    print(a,b)
printer(b=4,a=5)  #order not important


#default arguement

def printer(a,b=0):
    print(a,b)
printer(3) #i just only pass one value but it doesnot raise coz of default
         # but if i pass some value it overrides the default value


#*args → variable positional arguments
def add(*args):
    print(type(args))   #it is stored as tuple variable positional arguements
    return sum(args)

print(add(1,2,3,4,4)) 


#**argv -> variable keyword arguments
def data(**kargs):
    print(type(kargs))     #it is stored as a dictionary 
    print(kargs)
data(a="a",b="b",c="c")


#Keyword-only arguments (*)
def data(*,a,b):
    print(a,b)
data(a=3,b=4)


#order for arguments
def func(positional, default=10, *args, kw_only=5, **kwargs):
    pass


#in python function can return multiple values(tuple unpacking) 
def calc(a, b):
    return a+b,a-b       #if a fuction returns only one thing ,its type depends 
                          #what it is,if return 4 it is int 
                          #but in the case of multiple returing its always tuple
print(type(calc(5, 3)))
#print(x,y,z)



#function inside function

def first():
    print("this is first")
    def second():
        print("this is second")

    second()

first()


def func1():
  a = 'sushma'
 
  def func2():
    print(a)
  func2()
 
# driver code
func1()
#func2()  # we cannot call the func2 from here cause its inside the func1 so when python check for func2
           #it cant get func2





"""
namak closure padikam ,enik manasilaye ann ivide ezhuthi vekkune ,ippa namalk oru function ond outer
athinte akath oru variable ond count and athinte akath oru inner function kude ond function nte oru varable 
inner use akkunnum ond ,outer function inner nte object return chyum ennit nammal aa object vech call cheytha count nte value
remembered ayirikum ath closure cell store akum
"""
def outer():
    x=10
    def inner():
        nonlocal x  #by using nonlocal keyword we can define a variable which is in its external scope
        x=x+1
        print(x)
    return inner
f=outer()
f() #11
f() #12
print(f.__closure__) #we can see the closure 

"""
Lambda functions 
"""
# funcname= argument :expression 
square=lambda a:a*a
print(square(6))
print(type(square))



"""
map fuction (mapping cheyanda function,iterable um) eeach element of the iterable passes throu
gh what we defined functions
"""


l=[1,2,3,4,5]

def square(a):
    return a**2


l1=list(map(square,l))

l2=map(lambda a:a**2,l) #aa square enna function pakaram lambda use akkiye
""" ivide lab"""
print(l1)
print(list(l2))

"""
filter (filtering function,iterable)
"""
def is_even(a):
    if(a%2==0):
        return True
    
t=[1,2,3,3,4,5,6,35]
t1=tuple(filter(is_even,t))
print(t1)

#ith thanne lambda function vech cheyam
t2=list(filter(lambda a:a%2==0,t))
print(t2)



from functools import reduce 

"""
we can reduce somthing into one 
"""
m=[1,2,3,4,5]
print(sum(m))
print(reduce(lambda a,b:a*b,m)) #take two values multiply them 
