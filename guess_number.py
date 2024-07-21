import random

secret_number=random.randint(1,10)
user_number=int(input("Enter a number to guess = "))

if secret_number==user_number:
    print(f"you won")
else:
    print(f"You lost.The number was {secret_number}")