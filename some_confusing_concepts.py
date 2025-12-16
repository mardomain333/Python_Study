"""
1:::Difference between == and  is

== check the values is same 
is check whethe both are point to same object
"""
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b) #True
print(a is b) #false coz even though they have same values they 
              #they created as different objects
print(id(a),id(b)) #different memory 

a=b #here actaully we does not copy the the value of b to a 
     #but set the addrress(object address of b to a)
print(id(a),id(b))    

print(a==b)   #true
print(a is b) #true
              #(so if we do some change in b it will also reflect in a also)

b.append(5)
print(a,b)

"""but in python for small variables like intergers cache is there"""
#example
a=5
b=5
print(a==b)   #true
print(a is b)  #true (even though different objects are created python assign to same object for memeory effiency)





#mutable default argument
def add_item(item, lst=[]):
    lst.append(item)
    return lst
                    
print(add_item(1))
print(add_item(2))
print(add_item(3))
"""
concept : here there is a defualt argument lst=[] it will create once 
reused later
"""

def add(lst):
    
    lst.append(5)
    print(id(lst))
l=[1,2.3,4]
print(id(l))
add(l)
print(l)

def add(a):
    print(id(a))
    a=5
    print(id(a))
    print(a)
b=6
print(id(b))
add(b)
print(b)


#true=1,false=0
print(True+True+False+4) 
       #1    1    0    4 =6


# Empty collections and 0 are treated as False
if []:

    print("A")
elif {}:
    print("B")
elif 0:
    print("C")
else:
    print("D")

"""
Removing elements while looping causes index shifting and skipped values

"""
l=[1,2,3,4,5]
for i in l:
    l.remove(i)
print(l) #[2,4] skipped due to index shifting



"""
slicing property to override 1 mentioned thing
"""
a=[1,2,3,4]
b=a[:]
b.append(5)
print(a,b) #both are different coz due to slcing the only the values are 
           #transferd not the memory

"""
Function return vs print
"""
def func():
    print("hello")

a=func()
print(a) #None as it doesnt return anything



"""
Late binding (very tricky)
"""
funcs = []
for i in range(3):
    funcs.append(lambda: i) #ivide i nte address 3 times funcs enna 
                              #list store cheyum,last i=2 akumallo so 
                              
for f in funcs:
    print(f(), end=" ") #oro fun ayit vilikum so return 2 cheyum so ans 2 2 2
print()

"""
Tuple mutability trap
"""                          
        
t = (1, [2, 3])
t[1].append(3)

print(t)
