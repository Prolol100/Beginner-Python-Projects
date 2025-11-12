import random
import time
import sys

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)  
        sys.stdout.flush()
        time.sleep(delay)
    print()
options = ['rock', 'paper', 'scissor']
ai_choice = random.choice(options)

while True:
    user_choice = input('Enter choice:').lower()
    if not user_choice in options:
        print(f'Please choose between {options}')
        continue
    else:
        print('Rock', end = '')
        time.sleep(0.5)
        slow_print('...', 0.1)
        print('Paper', end = '')
        time.sleep(0.5)
        slow_print('...', 0.1)
        print('Scissor', end = '')
        time.sleep(0.5)
        slow_print('...', 0.1)
        print('Shoot')
        time.sleep(0.5)
        print(f'Your choice:{user_choice}')
        print(f'Computer\'s choice:{ai_choice}')
        if (user_choice == 'rock' and ai_choice == 'scissor') or \
        (user_choice == 'paper' and ai_choice == 'rock') or \
        (user_choice == 'scissor' and ai_choice == 'rock'):
            print('You win')
        elif user_choice == ai_choice:
            print('Its a draw')
        else:
            print('You lose')
    break