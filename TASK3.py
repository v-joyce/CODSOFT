#PASSWORD GENERATOR
import random
import string
print("Welcome to the Automatic Password Generator!")
length = int(input("Enter the length of password required: "))  
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
password = "".join(random.sample(all,length)) 
print(f"The password generated is: {password}")
