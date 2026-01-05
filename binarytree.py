
class node:
    def __init__(self,value):
         self.value=value
         self.left=None
         self.right=None
class Queue:
     def __init__(self):
          self.queue=[]
     def enq(self,value):
          self.queue.append(value)
     def deq(self):
          if len(self.queue):
              return self.queue.pop(0)
     def peek(self):
          if len(self.queue):
               return self.queue[0]
     def __len__(self):
          return len(self.queue)
          

class Binarytree:
     def __init__(self,root):
          self.root=node(root)

     def add_left(self):
          newnode=node(input("enter the left child"))
          self.root.left=newnode
        
     def add_right(self):
          newnode=node(input("enter the right child"))
          self.root.right=newnode

     def preorder(self,start,li):
           if start is None:
                return 
           li.append(start.value)
           self.preorder(start.left,li)
           self.preorder(start.right,li)
           return li
     def inorder(self,start,li):
           if start is None:
                return 
          
           self.inorder(start.left,li)
           li.append(start.value)
           self.inorder(start.right,li)
           return li
     def postorder(self,start,li):
          if start is None:
                return 
          
          self.postorder(start.left,li)
          self.postorder(start.right,li)
          li.append(start.value)
          return li
     def levelorder(self,start):
          li=[]
          queue=Queue()
          queue.enq(start)
          while(len(queue)>0):
               if queue.peek().left:
                   queue.enq(queue.peek().left)
               if queue.peek().right:
                   queue.enq(queue.peek().right)
               li.append(queue.peek().value)
               queue.deq()
          return li



tree=Binarytree(4)
tree.root.left=node(1)
tree.root.right=node(0)
tree.root.left.left=node(5)
tree.root.left.right=node(8)
tree.root.right.left=node(3)
tree.root.right.right=node(9)
print("DFS")
li=tree.preorder(tree.root,[])
print("preorder=",li)
li=tree.inorder(tree.root,[])
print("inorder=",li)
li=tree.postorder(tree.root,[])
print("postorder=",li)
print("BFS")
li=tree.levelorder(tree.root)
print("level order=",li)