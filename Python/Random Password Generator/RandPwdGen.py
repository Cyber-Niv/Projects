#Random Pasword Generator
import random
print("Welcome to password generator")
randomchar = "abcdABCD1234!@#$"
noofpwd = int(input("Enter the number of Passwords to be generated: "))
pwdlen = int(input("Enter the Password Length: "))
print("Generated passwords are:")
for x in range(noofpwd):
    pwd = ""
    for char in range(pwdlen):
        pwd = pwd+random.choice(randomchar)
    print(pwd)
