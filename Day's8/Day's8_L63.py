alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def display(msg, list):
    for i in list:
        msg += i
    return msg

user_again = True
while user_again:



    user_wanna = int(input("Enter '0' if you wanna Encrypt or '1' if you wanna Decrypt: "))
    if user_wanna == 0:
        plain_text = input("Enter the plain text: ").lower()
        shift_key= int(input("Enter the shift key value:"))

        cipher_text_list =[]
        for word in plain_text:
            if word not in alphabet_list:
                cipher_text_list.append(word)
            else:
             # cipher_value = (cipher_alphabet_list.index(word) + shift_key)%26
             # cipher_text = cipher_alphabet_list[(cipher_alphabet_list.index(word) + shift_key)%26]
             cipher_text_list.append(alphabet_list[(alphabet_list.index(word) + shift_key)%26])
             # print(f"cipher text: {cipher_value}({cipher_text}) ")

        encrypted_msg=""
        encrypted_msg = display(encrypted_msg, cipher_text_list)
        print(f"Encrypted msg : {encrypted_msg}")


    elif user_wanna == 1:
        cipher_text = input("Enter the cipher text: ").lower()
        shift_key= int(input("Enter the shift key value:"))

        plain_text_list =[]
        for word in cipher_text:
            if word not in alphabet_list:
                plain_text_list.append(word)
            else:
             plain_value = (alphabet_list.index(word) - shift_key)%26
             plain_text = alphabet_list[plain_value]
             plain_text_list.append(plain_text)


        decrypted_msg=""
        decrypted_msg =display(decrypted_msg, plain_text_list)
        print(f"plain text: {decrypted_msg}")

    else:
        print("Enter 0 for Encrypt or 1 for Decrypt")

    user_choice = (input("You want again to run y/n:")).lower()
    if user_choice == 'y':
        user_again = True
    elif user_choice == 'n':
        user_again = False
    else:
        print("Enter valid input")
        user_again = False