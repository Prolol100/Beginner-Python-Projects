import string

password_correct = False #Checks if password is correct
password = input("Enter your password: ")

while not password_correct:
 if len(password) < 8: #Checks the length of password
    print("Password must be at least 8 characters long.")
    password = input("Enter your password: ")
 elif not any(character.isupper() for character in password): #Checks for uppercase letter
    print("Password must contain at least one uppercase letter.")
    password = input("Enter your password: ")
 elif not any(character.islower() for character in password): #Checks for lowercase letter
    print("Password must contain at least one lowercase letter.")
    password = input("Enter your password: ")
 elif not any(character.isdigit() for character in password): #Checks for numbers
    print("Password must contain at least one digit.")
    password = input("Enter your password: ")
 elif not any(character in string.punctuation for character in password): #Checks if the password has special characters
    print("Password must contain at least one special character.")
    password = input("Enter your password: ")
 elif any(character.isspace() for character in password): #Checks if there are spaces in the password
    print("Password must not contain any space.")
    password = input("Enter your password: ")
 else:
    print(f"Your password {password} is valid.")
    password_correct = True