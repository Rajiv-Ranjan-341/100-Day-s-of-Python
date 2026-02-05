import random
Letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
number =['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','&','*']

print("!!Welcome in Password generator!!")
user_letter = int(input("How many letters do you want in password:"))
user_number = int(input("How many number do you want in password:"))
user_symbol = int(input("How many symbol do you want in password:"))

password =""

# for i in range(0, user_letter):
#     # ch = random.choice(Letter)
#     # print(ch)
#     # password += ch
#     # print(password)
#
#     password += random.choice(Letter)
# # print(password)
#
# for i in range(0, user_letter):
#
#     password += random.choice(number)
# # print(password)
#
# for i in range(0, user_letter):
#
#     password += random.choice(symbol)
#
# print(password)

#Hard password
password_list =[]
for i in range(0, user_letter):
    password_list.append(random.choice(Letter))


for i in range(0, user_letter):
    password_list.append(random.choice(number))


for i in range(0, user_letter):
    password_list.append(random.choice(symbol))


random.shuffle(password_list)
print(password_list)

for i in range(0,len(password_list)):
    password += random.choice(password_list)
print(password)
