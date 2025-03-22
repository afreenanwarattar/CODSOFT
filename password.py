import string 
import random

upper_case=string.ascii_uppercase
lower_case=string.ascii_lowercase
num=string.digits
sym=string.punctuation

all= upper_case + lower_case + num + sym 

opt= input("Want your own password ?  (yes/no): ").strip().lower()

if opt == "yes":
    pwd = input("Enter your password: ")
else:
    size= int(input("Put the size of the password: ")) 
    pwd = "".join(random.sample(all, length))  

print("Your password:", pwd)