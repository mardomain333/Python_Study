l=[5,2,2,1,1,1,-1,4]
prefixsum=0
deco={}
target=0
count=-1
deco[0]=count
maximum=0
for a in l:
    prefixsum+=a
    count+=1
  
    coco=prefixsum-target
    if coco in deco.keys():
        maximum=max(maximum,count-deco[coco])
        print(l[deco[coco]+1:count+1])
    else:
      deco[prefixsum]=count

print(maximum)
print(deco)

l=[1,2,3,4,5,6,6]

slide_size=4
left=0
right=4
maximum=sum(l[left:right])
temp=[]
temp=l[left:right+1]
print(maximum)
for r in range(right,len(l)):
   ground=maximum
   ground+=l[r]
   ground-=l[left]
   left+=1
   if ground>maximum:
      maximum=ground
      temp=l[left:r+1]
   
print(maximum)
print(temp)

l=[-2,3,-1,2]
#=[5, -2, 3, -4]
start=end=temp=0
currsum=l[0]
globalsum=currsum #kadane's algorithm
temp
for i in range(1,len(l)):
   if l[i]>currsum+l[i]:
      currsum=l[i]
      temp=i

   else:
      currsum+=l[i]
   if currsum>globalsum:
      globalsum=currsum
      start=temp
      end=i

print(globalsum)
print(l[start:end+1])

def binary_search(l,start,end,target):
   if start>end:
      return -1
   mid=(start+end)//2
   if l[mid]==target:
      return mid
   elif l[mid]<target:
      return binary_search(l,mid+1,end,target)
   elif l[mid]>target:
      return binary_search(l,start,mid-1,target)
def binarysearch(l,target):
   start=0
   end=len(l)-1
   
   while(start<=end):
      mid=(start+end)//2
      if l[mid]==target:
         return mid
      elif l[mid]<target:
         start=mid+1
      elif l[mid]>target:
         end=mid-1
   return -1

      
   
l=[1,2,3,4,5,6]
print(binarysearch(l,6))
print(binary_search(l,0,len(l)-1,4))




from module_study.calc import add

print(add(4,5))
def fact(n):
   if n==0 or n==1:
      return 1
   else:
      return n*fact(n-1)
print(fact(5))