from ast import operator
from re import T


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return  x/y
    else:
        return "Error! division by zero."
def calculator():
    print("welcome to the simple calculator")
    print("select any number of your choice")
    print("1. Addition")
    print("2. multiplication")
    print("3. subtraction")
    print("4. division")

    choice = input("Enter Chpice 1/2/3/4: ")

    if choice in ['1','2','3','4']:
       try:
          num1 = float(input("Enter first number:"))
          num2 = float(input("Enter second number:"))
       except ValueError as error:
           print("invalid input! please enter a numeric value.")
           return

    if choice == '1':
        print(f"{num1} + {num2}  {add(num1,num2)}")
    elif choice == '2':
        print(f"{num1} * {num2}  {multiply(num1,num2)}")
    elif choice == '3':
        print(f"{num1} - {num2}  {subtract(num1,num2)}")
    elif choice == '4':
        print(f"{num1} / {num2}  {divide(num1,num2)}")
    else:
        ("Enter a numeric value!!!")
        return

calculator()


