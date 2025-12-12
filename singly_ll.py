class node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

def display_ll(head):
    curr=head
    if curr.next==None:
        print(curr.value)
    else:
        string=""
        print("\n")
        while curr:

            string=string+f'{curr.value}->'
            curr=curr.next
        print(string)
          
        
def add_atbeg(head):
   curr=head
   value=int(input("enter the value"))
   new_node=node(value)
   return new_node
   
def add_atend(head):
    curr=head
    value=int(input("enter the value"))
    while curr.next!=None:
        curr=curr.next
    curr.next=node(value)
    



def delete_atend(head):
    prev,curr=head,head
    while(curr.next!=None):
        if curr==head:
            curr=curr.next
        else:
            curr=curr.next
            prev=prev.next
    return prev

def add_atindex(head,n,value):
    count=1
    curr=head
    prev=head
    while(count!=n):
        if count==1:
            curr=curr.next
            count+=1
        else:
            curr=curr.next
            prev=prev.next
            count+=1
    new_node=node(value)
    new_node.next=prev.next
    prev.next=new_node


def delete_atindex(head,n):
    count=1
    curr=head
    prev=head
    while(count!=n):
        if count==1:
            curr=curr.next
            count+=1
        else:
            curr=curr.next
            prev=prev.next
            count+=1
    prev.next=curr.next
try:   
    print("=====LINKED LIST PROGRAM=====")
    if input("\ndo u want to create a linked list(yes/no)")=='y':
        value=input("enter the value")
        head=node(value)
        print("\nlinked list created successfully")
        flag1=int(input("\ndo u want another option(1/0)"))
        while flag1!=0:
            print("===linked list options===")
            n=int(input("1>Display\n2>Add element at beg\n3>add element at end\n4>delete at begining\n5>delete at end\n6>enter at index\n7>remove at index\n0>exit\n"))
            match n:
                case 1:
                    display_ll(head)
                
                    
                case 2:
                    new_node=add_atbeg(head)
                    new_node.next=head
                    head=new_node
                    print("Element added at beginging")
                    display_ll(head)

                case 3:
                
                    add_atend(head)
                    print("Element added at end")
                    display_ll(head)

                case 4:
                    head=head.next
                    print("Element deleted at beginging")
                    display_ll(head)

                case 5:
                    end=delete_atend(head)
                    end.next=None
                    print("Element deleted at ending")
                    display_ll(head)                
                    
                case 6:
                    value=int(input("enter the value"))
                    n=int(input("enter the index"))
                    if n==1:
                        add_atbeg(value)
                    else:
                        add_atindex(head,n,value)
                    print(f"Element added at index{n}")
                    display_ll(head)

                case 7:
                    n=int(input("enter the index"))
                    delete_atindex(head,n)
                    print(f"Element deleted at index{n}")
                    display_ll(head)
                case 0:
                    print("Existing.....")
                    break
except:
    print(">>>>>><<<<< Something went wrong !!!>>>><<<<<")
                

       

 