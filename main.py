import os
import random
from datetime import datetime

from characters import letters, numbers, symbols

# Easy Level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard level
def generate_password():
    print("Welcome to the PyPassword Generator!")
    password_for = input("What is this password for? (e.g., Gmail, Netflix, etc.): ")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password_list = []
    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))

    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
        
    return password_for, password

def save_password(password_for, password):
    # Define the specific path for password.txt
    file_path = os.path.join(os.path.dirname(__file__), "password.txt")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"[{timestamp}] {password_for}: {password}\n")

def main():
    password_for, password = generate_password()
    print(f"\nYour password for {password_for} is: {password}")
    save_password(password_for, password)
    print("Password has been saved to password.txt")

if __name__ == "__main__":
    main()

