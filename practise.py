

#kadane 's algorithm for max sub array sum


arr=[1,2,3,6,4,5,6]

globalsum=arr[0]
currentsum=arr[0]
start=end=temp=0

for i in range(1,len(arr)):
    if arr[i]>arr[i]+currentsum:
        currentsum=arr[i]
        temp=i
    else:
        currentsum+=arr[i]
    if currentsum>globalsum:
        globalsum=currentsum
        start=temp
        end=i
print('maximumsum',globalsum)
print("occured at",arr[start:end+1])



#coco prefixsum algorithm for finding the sublistwith sum=k


arr1=[1,1,1,1,2,2,5,-1,4]
arr1=[1,4,6,3,23,3,4,32,2]
arr=[1 if i&1 else -1 for i in arr1]

count=-1
prefixsum=0
k=0
dic={

}
dic[prefixsum]=count
minimum=999
maximum=0
for a in arr:
    prefixsum+=a
    count+=1
    coco=prefixsum-k
    if coco in dic.keys():
        doco=count-dic[coco]
        maximum=max(maximum,doco)
        minimum=min(minimum,doco)
        print(arr1[dic[coco]+1:count+1])

    dic[prefixsum]=count
print(maximum)
print(minimum)


print("===========================================================")

#fixed sliding window to find the max sum for a window k

arr=[1,1,1,3,2,1,2,3,4]

k=4

total=sum(arr[:k])
largest=total
l=0
start=l
end=k

for r in range(k,len(arr)):
    total-=arr[l]
    total+=arr[r]
    l+=1
    if total>largest:
        largest=total
        start=l
        end=r
print(largest)
print(arr[start:end+1])

#longest substring without repating characters

#dynamic sliding window


string="adjflkjsfie"

l=r=0
long=0
repeated=set()
for r in range(len(string)):

    while(string[r] in repeated):
        repeated.remove(string[l])
        l+=1

    repeated.add(string[r])
    if long<(r-l)+1:
        long=(r-1)+1
        start=l
        end=r
print(long)
print(string[start:end+1])


print("=================================================")
Input= "aabacbebebe" 
k=3
l=0
dic={}
long=0
start=end=0
for r in range(len(Input)):
   dic[Input[r]]=dic.get(Input[r],0)+1
   while(len(dic)>k):
        dic[Input[l]]-=1
        if dic.get(Input[l])==0:
            del dic[Input[l]]
        l+=1
   if long<(r-l)+1:
        long=(r-l)+1
        start=l
        end=r
print(long)
print(Input[start:end+1])