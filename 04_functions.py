#FUNCTIONS

def whoami(): #this is a function without parameters

    name = "Omkar" #local variable
    age = 21 #local variable
    print("My name is " + name + " and I am " + str(age) + " years old.") #printing the local variables

whoami()

def add_one_hundred(num): #function with a parameter

     print(num + 100) 

add_one_hundred(100)


def add(x, y): #function with two parameters

    print(x + y)

add(1, 2)

def multiply(x, y): #function that returns a value

    return x * y

print(multiply(2, 3))   


def square_root(x): #function that returns the square root of a number
    print(x ** 0.5)
square_root(16)


def nl(): #function to print a new line
    print("\n")
nl()

