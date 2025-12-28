l=[9,4,20,3,10,5,-1]      #maximum subarray sum equals target
l=[5,2,2,1,1,1,1,4]
target=4

hastmap={}
count=-1
prefixsum=0
hastmap[0]=count
maxvalue=99
coco=0
for a in l:
    count+=1
    prefixsum+=a
    dono=prefixsum-target
    if dono in hastmap.keys():
          maxvalue=count-hastmap[dono] if maxvalue> (count-hastmap[dono]) else maxvalue
          coco+=1
          print(l[hastmap[dono]+1:count+1])
    hastmap[prefixsum]=count
print(hastmap)
print(maxvalue)


