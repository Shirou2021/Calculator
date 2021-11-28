# Create a simple calculator 
import sys
import re

# checks for version of python 3
print ("Hello Python", sys.version)

# 5 different function for 5 most common mathematical operations!
def addition (num1, num2):
	sum = num1 + num2
	return sum

def subtraction (num1, num2):
	sum = num1 - num2
	return sum

def multiplication (num1, num2):
	sum = num1 * num2
	return sum

def division (num1, num2):
	sum = num1 / num2
	return sum

def modulo (num1, num2):
	return num1 % num2

first = float(input("Enter first value: "))
second = float(input("Enter second value: "))
userInput = input("Enter an operation + - * / %: ")

# Lines 41 to 45 checks for only integet input.
firstCheck = re.compile(r'^\-?[1-9][0-9]*$')
checkPassed1 = re.match(firstCheck, userInput)

secondCheck = re.compile(r'^\-?[1-9][0-9]*$')
checkPassed2 = re.match(secondCheck, userInput)

validate = True
while validate:
	# A tradition way to check for user input. Could be done in function 
	if (userInput == "+" or "-" or "*" or "/" or "%" and checkPassed1 and checkPassed2):
		if userInput == '+':
			print ("Result: ", addition(first, second))
		elif userInput == '-':
			print ("Result: ", subtraction(first, second))
		elif userInput == '*':
			print ("Result: ", multiplication(first, second))
		elif userInput == '/':
			if (second != 0):
				print ("Result: ", multiplication(first, second))
			else:
				print ("Error! Unable to divide by 0")  
				exit(0)
		elif userInput == '%':
			print ("Reminder: ", modulo(first, second))

	else:
		print ("Invalid selection entry!")
		exit(0) # If no valid entry was entered, end the program and start over!
	validate = False

