N = 2
hallA = [12, 11]
hallB = [10, 7]
total=sum(hallA)
print("if all goes to hallA",total)
dif=[hallB[i]-hallA[i] for i in range(N)]
print(dif)
dif.sort()
for i in range(N//2):
    total+=dif[i]
print(total)

