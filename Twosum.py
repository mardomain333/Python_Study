l=[1,2,2,3,4,5]
target=5

serve={

}
for i in range(len(l)):
    if target-l[i]in serve.keys():
        print(serve[target-l[i]],i)
    else:
        serve[l[i]]=i

