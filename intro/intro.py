print("Hello from Python")

# single line  comment

"""
multi
line
comment
"""

# variables and variable types
name = "Corey"
print(name)

age = 98
total = 19.99
found = True 

print(age)
print(total)
print(found)
print(name + name) # String concatination
print(age + 1) # sum
print(name +str(age))

if(age < 100):
    print("You are still young")
    print("Another line inside if")
elif (age == 100):
    print("You are on the very edge :p")
else:
    print("Sorry you are just old")

print("Line outside the if")


# definition of a function
def test():
    print("Hello I'm a test")


test() # call / exec a function  
test()

