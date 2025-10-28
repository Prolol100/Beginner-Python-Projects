def avg_calc(prompt,text):
    '''This function calculates the average of a list of numbers provided as a space-separated string.'''
    a = True
    while a:
        try:
            n = list(float(i) for i in input(prompt).split()) #This converts the input into a list of floats
            if not n: #Checks if list is empty
                print("No numbers entered. Please try again.")
            else: #Calculates the average and prints it
                print(text,sum(n)/len(n))
                a = False
        except ValueError:
            print("Invalid input. Please enter numbers only.")

avg_calc('Enter the marks separated by spaces:','The average marks is:')
avg_calc('Enter the prices separated by spaces:','The average price is:')


