
l=[9,4,20,3,10,5,-1]
l=[5,2,2,1,1,1,1,4]
target=6

#here we have to find the max length of  substring that will have the sum of target
#in the given list [2,2] [1,1,1,1] [4] these substrings have the sum of 4 

#here we use prefixsum + hashmap technology 
counter=0
prefixsum=0
maxvalue=0
minvalue=0
count=-1
di={} #hash map to store the prefix sum and index that obtained
di[0]=count #just initializing the hashmap {0:-1} {prefixsum:index}
#iterate through the list
for a in l:
    prefixsum+=a           #ADDING THAT ELEMENT TO PREFIX SUM
      
    count+=1
   
    dono=prefixsum-target   #JUST MINUS THE CURRENT PREFIX SUM WITH TARGET SO                       WE CAN GET A SUM WHICH 
    if dono in di.keys():
        cono=count-di[dono]
        maxvalue=cono if maxvalue < cono else maxvalue
        minvalue=cono if maxvalue > cono else minvalue
        print(l[di[dono]+1:count+1])
        counter+=1
    di[prefixsum]=count
   
print(f"max lenght={maxvalue}")
print(f"min length={minvalue}")
print(f"no of sublist={counter}")