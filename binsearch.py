l=[0,1,2,3,4,5]
def linear_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    else:
        return -1
    

def binary_search(li,target):
    l=0
    r=len(li)-1
    
    while(l<=r):
        mid=(l+r)//2
        if li[mid]==target:
            return mid
        elif li[mid]<target:
            l=mid+1
            
        else:
            r=mid-1

    return -1

def bin_search(arr,l,r,target):
    if l>r:
        return -1
    mid=(l+r)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return bin_search(arr,mid+1,r,target)

    else:
        return bin_search(arr,l,mid-1,target)
    
print(linear_search(l,14))
print(binary_search(l,14))
print(bin_search(l,0,len(l)-1,14))