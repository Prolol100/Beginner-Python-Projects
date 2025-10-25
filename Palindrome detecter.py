string = input("Enter a string: ").replace(" ", "").lower()

string1 = string[::-1]

if string == string1:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")