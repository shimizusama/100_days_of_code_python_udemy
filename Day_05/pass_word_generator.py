#this is a passord generator for day five
#by watching 100 days of code i've leraned python lists and randomization, but i've searched the web for better algorithms and security.


import secrets
import string

letters = string.ascii_letters # it brings all letterw, it saves me from typing the whole alphabet
digits = string.digits # It saves me from typing 0-9
symbols = "!@@#$%¨&*()[]{}" # i didnt found a library the has it.

#get user input
num_letters = int(input("How many letters? \n"))
num_digits = int(input("How many digits? \n"))
num_symbols = int(input("How many symbols? \n"))

#generate the list

password_list = [] #empty string

for num in range(num_letters):
    password_list.append(secrets.choice(letters))  # this part python goes to the string letters and Choose num_letters randomly. Its safer to use secrests than normal random
for num in range(num_digits):
    password_list.append(secrets.choice(digits))
for num in range(num_symbols):
    password_list.append(secrets.choice(symbols))

#this will shufle the list
secrets.SystemRandom().shuffle(password_list)

final_passwd = "".join(password_list) #join will joins the string together for better loking
print("Your Passwd is: \n", final_passwd)
