notes = {
    100: 10,
    200: 2,
    500: 1
}
amount = 900

sat=amount
f=0
t=0
o=0
while(sat>0):
    if sat>=500 and notes[500]>0:
        sat-=500
        notes[500]-=1
        f+=1
    elif sat>=200 and notes[200]>0:
        sat-=200
        notes[200]-=1
        t+=1
    elif sat>=100 and notes[100]>0:
        sat-=100
        notes[100]-=1
        o+=1
    else:
        print("note required..")
        break
print("500x",f)
print("200x",t)
print("100x",o)

arrival = [900, 940, 950, 1100, 1500]
departure = [910, 1200, 1120, 1130, 1900]
count=1
for i in range(len(arrival)-1):
    if arrival[i+1]>departure[i]:
        continue
    else:
        count+=1
print(count)



intervals = [[0,30],[5,10],[15,20]]
start=[]
stop=[]
for a in intervals:
    start.append(a[0])
    stop.append(a[1])
start.sort()
stop.sort()
i=j=0
minimum=0
while(j<len(intervals)or i<len(intervals)):
    if start[i]>stop[j]:
        minimum+=1
        i+=1
    else:
        break
print(minimum)