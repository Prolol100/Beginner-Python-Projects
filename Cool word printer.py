import time
import string

text = input('Enter a word: ')
temp = ''

for char in text: #Prints the text in a cool way
    if char == ' ':
        temp += ' '
        continue
    for i in string.ascii_letters:
        time.sleep(0.05)
        print(temp + i)
        if i == char:
            temp += i
            break
        