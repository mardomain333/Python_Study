
class car:
    pass

bmw=car()
bens=car()

print(bmw is bens) #false because both are different objects and different memory

#Here is the thought of singleton class 
#main concept is that we can only create a object from that class

class inventory:
    _instance=None                             #__new__ is the first function when an object 
                                                 #python automatically done this for us ,but in case we have to restrict this
    def __new__(cls):
        if cls._instance is None:
          cls._instance=super().__new__(cls)
        return cls._instance
a=inventory()
b=inventory()

print(a is b) # True because first object normal creation after that each new object will
#will get the same instance of first object 




class user:
    def __init__(self,Name,id):
        self.id=id
        self.name=Name
        self.is_active=True
        self.balance=0
    def updation(self):
        print(self.name,"notificaton recived")
    

class system:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.userlist=[]
    def subscribe(self,*users):
        self.userlist.extend(users)
    def unsubcribe(self,name):
         users = [user for user in self.userlist if user.name==name]
         for user in users:
             user.is_active=False
    
    
    def notify(self):
        users=[user for user in self.userlist if user.is_active == True]
        for user in users:

            user.updation()

s=system()
gokul=user("Gokul",1)
akul=user("akul",2)
s.subscribe(gokul,akul)
s.notify()
s.unsubcribe('akul')
s.notify()