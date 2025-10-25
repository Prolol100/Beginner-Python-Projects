import random

number = random.randint(0, 100)

tries = 0

while tries <= 5:
    try:
        user_input = int(input("Guess a number between 0 and 100 in 5 tries: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    tries += 1

    if user_input < number:
        if number - user_input <= 5:
            print("Slightly low!")
        elif number - user_input <= 20:
            print("Moderately low!")
        else:
            print("Very low!")    
    elif user_input > number:
        if user_input - number <= 5:
            print("Slightly high!")
        elif user_input - number <= 20:
            print("Moderately high!")
        else:
            print("Very high!")
    else:
        print(f"Congratulations! You've guessed the number {number} in {tries} tries.")
        break

if tries > 5:
    print(f"Sorry, you've used all your tries. The number was {number}.")