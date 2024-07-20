print("~~~~~~~~~~~PASSWORD GENERATOR~~~~~~~~~")
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Please, enter the desired length of the password: "))

password = generate_password(length)
print("Generated password:", password)
print("Thank you")

