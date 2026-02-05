student_sccore = [123,34,199,64,42,35,32,12,44,21,67,6,75,14,66,75,45,76,87]

# print(max(student_sccore))
maxi=0
for stu in student_sccore:
    if stu >maxi:
        maxi =stu
print(maxi)

# print(sum(student_sccore))
# create above function
sum=0
for stu in student_sccore:
    sum+=stu
print(sum)
