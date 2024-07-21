import random

secret_number = random.randint(1, 13)
user_number = int(
    input("Enter a number to guess (above, below,or equal to 7) upto 13 = ")
)

if 1 <= secret_number < 7 and 1 <= user_number < 7:
    print(f"You win!")
elif 7 < secret_number <= 13 and 7 < user_number <= 13:
    print(f"You win!")
elif 1 <= secret_number < 7 and 7 < user_number <= 13:
    print(f"Sorry,you lose.")
elif 7 < secret_number <= 13 and 1 <= user_number < 7:
    print(f"Sorry,you lose.")
elif user_number == 7 and secret_number == 7:
    print(f"You win!")
elif user_number == 7 and secret_number != 7:
    print(f"Sorry,you lose.")
else:
    print(f"Invalid number")
