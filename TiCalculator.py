# Create a simple calculator 
import sys
import math

# checks for version of python 3
print(sys.version)		
print("Hello Python!!!")


num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))
userInput = input("Enter an operation + - * /: ")
validate = True
while validate:
	if userInput == '+':
		num1 + num2
		print ("Result: ", num1 + num2)
	elif userInput == '-':
		num1 - num2
		print ("Result: ", num1 - num2)
	elif userInput == '*':
		num1 * num2
		print ("Result: ", num1 * num2)
	elif userInput == '/':
		if num2 == '0':
			print ("Error! Denominator cannot be 0")
			break;
		if num2 != 0:
			num1 / num2
			print ("Result:", num1 / num2)
	validate = False

# <<<<<<< HEAD
# def addition:
# 	return 0;
# def substraction:
# 	return 0:
# def multiplication:
# 	return 0;
# def division:
# 	return 0;
# def modules:
# 	return 0;
# # Use tinker to generate mini calculator looking app.
# # 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
