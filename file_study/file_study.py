people=input("Enter the names separated by comma..").split(',')

people=set(people)

with open('peoples.txt','r') as file:
    near_people=file.readlines()
    file.close()
near_people=set(near_people)

near_people_list=people.intersection(near_people)
with open("peoples.txt",'a') as file:
 for names in near_people_list:
    print(f"Hey {names} is near to u ..")
    file.write(names+'\n')
file.close()

