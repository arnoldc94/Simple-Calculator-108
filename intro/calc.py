"""
System: Simple Calculator
Author: Corey Arnold
Functionality:
    - Sum
    - Subtract
    - Multiply
    - Divide
"""

# imports
from display import print_menu

# global vars
"""
    division
    if the user tries to divide by zero:
        show an error "asdldjfjj;ksd"
        result to 0

"""

# functions


# plain instructions
opt = ""
while(opt != "x"):

    print_menu()

    opt = input("Choose an option: ")
    if(opt == "x"):
        break

    if(opt != "5"):
        try:
            # ask for num1 and num2
            num1 = float(input("Enter num1: "))
            num2 = float(input("Enter num2: "))
            
        except:
            print("Invalid input, try again")
            continue

    
    if(opt == "1"):
        print(f"The result is: {num1 + num2}")

    elif(opt == "2"):
        print(f"The result is: {num1 - num2}")

    elif(opt == "3"):
        print(f"The result is: {num1 * num2}")

    elif(opt == "4"):
        if(num2 == 0):
            print("Error: Division by zero not allowed")
        else:    
            print(f"The result is: {num1 / num2}") 

    elif(opt == "5"):  
        phrase = input("Provide a message: ")
        count = input("Provide n: ")

        num = 0

        while(num < int(count)):
            print(phrase)
            num = num + 1
            

    input("Press Enter to continue...")       

print("Good bye")

