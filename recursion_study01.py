"""
mone recursion nammalk ariyavune karyam thanne simply paranja 
oru function calling itself so i can act as a loop isnt it 

"""
count=0
def infinity():
    global count
    count+=1
    print("name",count)
    infinity()
#infinity()           #yi infinity() de mumbil olle # mattiya thazhe olle th kanam
"""
nammal oro vettam oru fn call cheyumbol ath function stack ottu push cheyum
eppol ano execution kazhiyunne appo aa function stackil ninn pop cheym
but ivide oru infinity recursion pokuan so stack overflow akum. python ayond 999
function calls stack il push cheyth.oru function completely execution akanam enkil ividudthe case anusarich athinte akath olle function return akanam but ivide return akulla continous ayitt call cheythonde irikum 


so nammal pothuve condition set cheyth yi recursion ee controll cheyum

"""
#write a program to print ramu 4 times using recursion

"""
yi thazhe koduthekunne pgm ramu enn 4 vettan print cheyum 
        1.print_ramu()                    ^
                                          |
               v
        2.print_ramu()                    |
               |  checked count==4
                  print("ramu")           ^
                  count ++ //=1           |
               v
        3.print_ramu()                    ^
               |  
                  checked count==4        |
                  print("ramu")
                  count ++ //=2           ^
                v  
         4.print_ramu()                   |
                  checked count==4
                  print("ramu")
                  count ++ //=3           |
         5.print_ramu()                   ^   
                  checked count==4
                  print("ramu")           |
                  count ++  //=4
        6.print_ramu()                    ^
                  returned                |
                  |-----------------------|               
"""     

                         #ithine nammal Head recursion enn parayum
                                #namma print thazhott pokumbole chyunandallo
                                # output nokiyal kanam (count valu) 
                                #ramu 0
                                #ramu 1
                                #ramu 2
count=0                         #ramu 3
print("===Head Recursion===")
def print_ramu():
    global count
    if count==4:
        return 
    print("ramu",count)
    count+=1      
    print_ramu()

print_ramu()

"""
ini nammak tail recursion allel some kind of backtracking nokam ,ivide and last function vere jst call pokum pine back ott return  kitii aa function olle execute cheyth back ott verm 
"""
count=0 
                        
print("===Tail Recursion===")
def print_ramu():
    global count
    if count==4:
        return 
    count+=1      
    print_ramu()
    count-=1
    print("ramu",count)

print_ramu()



"""
recursion with sending the  parameter 
"""
#program to print 1 to 5
def printing(i,n):
       if i>n:
            return
       print(f"fun({i,n})")
       printing(i+1,n)
printing(1,6)

#i am just illustrating how tail will work 
print()
def printing(i,n):
     if i>n:
          return
     print(f"called fun({i,n})")
     printing(i+1,n)
     print(f"executed fun({i,n})")
printing(1,6)

#program to print 5 to 1
#head

def printer(n):
     if n==0:
          return
     print(n)
     printer(n-1)
printer(5)

#tail
def printer(n):
     if n==0:
          return 
     printer(n-1)
     print(n)
printer(5)