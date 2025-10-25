import random
import time

#x,y,z,A = random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9)
#print(f'(debug): {x}{y}{z}{A}')
try:
    x,y,z,A = (int(i) for i in input('Enter four digit password separated by spaces: ').split())
    if not all(0 <= digit <= 9 for digit in (x, y, z, A)):
        raise ValueError
except ValueError:
    print("Invalid input. Please enter four digits between 0 and 9.")
    exit()

print('Starting search for password...')

time.sleep(5)

if x == 6 and y == 7 and z == 6 and A == 7:
    print('Nice try Diddy')
else:
    for a in range(10):
        time.sleep(0.0025)
        for b in range(10):
            time.sleep(0.0025)
            for c in range(10):
                time.sleep(0.0025)
                for d in range(10):
                    time.sleep(0.0025)
                    print(f"Trying combination: {a}{b}{c}{d}")
                    if a == x and b == y and c == z and d == A:
                        print(f"Found it: {a}{b}{c}{d}")
                        exit()