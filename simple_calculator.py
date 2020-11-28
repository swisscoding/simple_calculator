#!/usr/local/bin/python3

import colored

print(colored.stylize("\n---- | Simple CLI-Calculator | ----\n", colored.fg("red")))


while True:
    print(colored.stylize("Options:", colored.fg("green")))
    print(">>> 'a' to add two numbers")
    print(">>> 's' to subtract two numbers")
    print(">>> 'm' to multiply two numbers")
    print(">>> 'd' to divide two numbers")
    print(">>> 'q' to end the program\n")
    user_input = input(": ")

    if user_input == "q":
        print()
        break
    elif user_input == "a":
        num1 = float(input("\nEnter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result + "\n")

    elif user_input == "s":
        num1 = float(input("\nEnter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result + "\n")

    elif user_input == "m":
        num1 = float(input("\nEnter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result + "\n")

    elif user_input == "d":
        num1 = float(input("\nEnter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is " + result + "\n")

    else:
        print("\nUnknown input\n")
