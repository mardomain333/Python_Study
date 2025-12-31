l=[1,2,2,3,4,5]
target=10
is_there=False
serve={

}
for i in range(len(l)):
    if target-l[i]in serve.keys():
        print(f"index {serve[target-l[i]],i}")
        print(f"values{l[serve[target-l[i]]],l[i]}")
        print("======================================")
        is_there=True
    else:
        serve[l[i]]=i
if not is_there:
    print("no pair ...")

