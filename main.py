list_stu=[]
for _ in range(int(input())):
    name = input()
    score = float(input())

    list_stu.append([name, score])


print(list_stu)

list_stu.sort(key=lambda x: x[1])

print(list_stu)


for i in range(1,len(list_stu)+1):
        if list_stu[i][1]==list_stu[i+1][1]:
            print(list_stu[i][0])
        else:
            print(list_stu[i-1][0])


