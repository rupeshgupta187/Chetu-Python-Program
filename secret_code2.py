import string
import random

def secret_code(input_str):
    input_str = input_str.lower()
    rev = input_str[::-1]
    
    print('''Choose character set for password from these :
            1. Digits
            2. Letters
            3. Special characters
            4. Exit''')

    choice = input("Enter your choice: ")
    if choice == '1':
        charlist = string.ascii_letters + string.digits
    elif choice == '2':
        charlist = string.ascii_letters
    elif choice == '3':
        charlist = string.punctuation
    elif choice == '4':
        return "Exiting..."
    else:
        return "Invalid choice"
    
    secret = []
    length = int(input("Enter the length of the secret code: "))
    for x in range(length):
        randchar = random.choice(charlist)
        secret.append(randchar)
    
    return "Random string is: " + "".join(secret)

input_str = input("Enter a string for encoding: ")
result = secret_code(input_str)
print(result)
