#math opteration
num1 = 5
num2 = 12

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 ** num2) #a and b = a^b
# print(num1 / num2)# like 2.67395842
# print(num1 // num2)# float to int like 2.6666 --->  2

#PEMDASLR

#()--> * --> / ---> + ---> - ---> left to right

print("result " + str(3 * 3 + 3 / 3 -3))


bmi = 84/(1.65**2)  # weight / height squ
print("BMI " + str(bmi))

# roundoff function
print(bmi) # ans is float
print(int(bmi)) # ans convert into int
print(round(bmi)) # ans roundoff to ...
print(round(bmi, 3)) # ans with only 3 decimal places