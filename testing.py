#kadane 

arr=[1,-2,3,4,-5,5]

globalsum=arr[0]
currentsum=arr[0]
start=end=temp=0
for i in range(1,len(arr)):
    if currentsum+arr[i]<arr[i]:
        currentsum=arr[i]
        temp=i
    else:
        currentsum+=arr[i]
    if globalsum<currentsum:
        globalsum=currentsum
        start=temp
        end=i
print("global:",globalsum)
print("array:",arr[start:end+1])

print("===================================")

#subarray sum=k
#coc prefixsum
arr=[1,1,1,1,2,2,4,5,-1]
k=4
prefixsum=0
count=-1
dic={}
dic[prefixsum]=count
minimum=999
maximum=0
for r in range(len(arr)):
    count+=1
    prefixsum+=arr[r]
    coco=prefixsum-k
    if coco in dic.keys():
        doco=count-dic[coco]
        maximum=max(maximum,doco)
        minimum=min(minimum,doco)
        print(arr[dic[coco]+1:count+1])
    dic[prefixsum]=count
print(dic)
print("max:",maximum)
print("min:",minimum)


#longest substring without repeating characters
print("=====================================================")

st="adjflkjsfie"

l=r=0
start=end=0
repeated=set()
maxlength=0
for r in range(len(st)):
    while(st[r] in repeated):
        repeated.remove(st[l])
        l+=1
    repeated.add(st[r])
    currlength=(r-l)+1
    if currlength>maxlength:
        maxlength=currlength
        start=l
        end=r
print(maxlength)
print(st[start:end+1])

print("================================================================")

Input= "aabacbebebe" 
k=3

l=0
dic={}
start=end=0
maximum=0
for r in range(len(Input)):
    dic[Input[r]]=dic.get(Input[r],0)+1
    while(len(dic)>k):
        dic[Input[l]]-=1
        if dic[Input[l]]==0:
            del dic[Input[l]]
        l+=1
   

    currlength=(r-l)+1
    if currlength>maximum:
        maximum=currlength
        start=l
        end=r
print(maximum)
print(Input[start:end+1])