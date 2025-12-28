#fixed size sliding window for finding 
#max sub avg

l=[1,12,-5,-6,50,3]
slidelength=4
maxsum=sum(l[:slidelength])
left=0
right=slidelength
for  a in range(slidelength,len(l)):
    sum=maxsum
    sum+=l[right]
    sum-=l[left]
    maxsum=max(maxsum,sum)
    right+=1
    left+=1
print(maxsum/4)



#max substring of lenth 4 have max vowels
def vowel_count(list):
    count=0
    vowels=['a','e','i','o','u']
    for a in list:
        if a in vowels:
            count+=1
    return count

string="gkkjl"
slide_len=2
r=slide_len
l=0
result=string[l:r]
max_vowels=vowel_count(string[:slide_len])

for i in range(slide_len,len(string)):
    l+=1
    r+=1
    sum=vowel_count(string[l:r])
    if max_vowels<sum:
        result=string[l:r]
    max_vowels=max(max_vowels,sum)
       
print(max_vowels)
print(result)