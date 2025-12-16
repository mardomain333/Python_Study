"""
selection sorting oro iteration vech cheriya element olla index kand
pidich frontil add cheythonde irikum .select akki frontil vekum
"""
def selection_sort(temp):

    size=len(temp)
    l=temp.copy()
    for i in range(size):
        j=i
        min=j                            
        while(j<size):
            if l[min]>l[j]:
                min=j
                j+=1
            else:
                j+=1
        l[i],l[min]=l[min],l[i]
    print(f"selection {l}")


"""
bubble sort comparing 2 adjacent elements aand swap them if need 
"""

def bubble_sort(temp):
    size=len(temp)
    l=temp.copy()
    for i in range(size):
        for j in range(size-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(f"bubble sort {l}")
    
        

temp=[10,5,4,1,6,8,4,14,24,32]
print(f"actual {temp}")
selection_sort(temp)
bubble_sort(temp)


