# ask user if they want to generate a password or not
# if yes, ask for password length
# generate password
# print password
# if initial response is no, exit program

import string
import random

chars = list(string.ascii_letters + string.digits + string.punctuation)


def generate_password():
    password_length = int(input("Input the number of characters: "))
    random.shuffle(chars)
    password = []

    for i in range(password_length):
        password.append(random.choice(chars))

    random.shuffle(password)
    password = "".join(password)
    print(password)


option = input("Do you want to generate a password? Y/N ")
if option.lower() == "y":
    generate_password()
elif option.lower == "n":
    print("Bye!")
    exit()
else:
    print("Invalid input, please use Y/N")
