# Use tkinter create a quick and simple calculator.
# Only intended to make it as a fun project. 

import tkinter as tk

calculation = ""

def intries(symbol):
  global calculation
  calculation = calculation + str(symbol) # handles integer and char intry
  text_result.delete(1.0, "end") # clear the screen after each use
  text_result.insert(1.0, calculation)

# A function that does some basic operation, like add, subtract, multiply, and etc
def math():
  global calculation
  try:
    calculation = str(eval(calculation))
    text_result.delete(1.0, "end") # clear the screen after each use
    text_result.insert(1.0, calculation)
  except:
    reset()
    text_result.insert(1.0, "Error. Unable to divide by 0!")

def reset():
  global calculation
  calculation = ""
  text_result.delete(1.0,"end")




root = tk.Tk()
root.title("Calculator")
root.geometry("280x430") # need to adjust, weight X height
text_result = tk.Text(root, height = 2, width = 16, font=("Times New Roman", 23))
text_result.grid(columnspan = 5)

# lambda will reference to the function instead directly using it.
button_0 = tk.Button(root, text = "0", command=lambda: intries(0), width=6, height = 3, font=("Times New Roman", 13))
button_0.grid(row = 5, column = 2)

button_1 = tk.Button(root, text = "1", command=lambda: intries(1), width=6, height = 3, font=("Times New Roman", 13))
button_1.grid(row = 4, column = 1)

button_2 = tk.Button(root, text = "2", command=lambda: intries(2), width=6, height = 3, font=("Times New Roman", 13))
button_2.grid(row = 4, column = 2)

button_3 = tk.Button(root, text = "3", command=lambda: intries(3), width=6, height = 3, font=("Times New Roman", 13))
button_3.grid(row = 4, column = 3)

button_4 = tk.Button(root, text = "4", command=lambda: intries(4), width=6, height = 3, font=("Times New Roman", 13))
button_4.grid(row = 3, column = 1)

button_5 = tk.Button(root, text = "5", command=lambda: intries(5), width=6, height = 3, font=("Times New Roman", 13))
button_5.grid(row = 3, column = 2)

button_6 = tk.Button(root, text = "6", command=lambda: intries(6), width=6, height = 3, font=("Times New Roman", 13))
button_6.grid(row = 3, column = 3)

button_7 = tk.Button(root, text = "7", command=lambda: intries(7), width=6, height = 3, font=("Times New Roman", 13))
button_7.grid(row = 2, column = 1)

button_8 = tk.Button(root, text = "8", command=lambda: intries(8), width=6, height = 3, font=("Times New Roman", 13))
button_8.grid(row = 2, column = 2)

button_9 = tk.Button(root, text = "9", command=lambda: intries(9), width=6, height = 3, font=("Times New Roman", 13))
button_9.grid(row = 2, column = 3)

button_plus = tk.Button(root, text = "+", command=lambda: intries("+"), width=6, height = 3, font=("Times New Roman", 13))
button_plus.grid(row = 4, column = 4)

button_minus = tk.Button(root, text = "-", command=lambda: intries("-"), width=6, height = 3, font=("Times New Roman", 13))
button_minus.grid(row = 3, column = 4)

button_multiplication = tk.Button(root, text = "*", command=lambda: intries("*"), width=6, height = 3, font=("Times New Roman", 13))
button_multiplication.grid(row = 2, column = 4)

button_division = tk.Button(root, text = "/", command=lambda: intries("/"), width=6, height = 3, font=("Times New Roman", 13))
button_division.grid(row = 1, column = 4)

button_decimal = tk.Button(root, text = ".", command=lambda: intries("."), width=6, height = 3, font=("Times New Roman", 13))
button_decimal.grid(row = 5, column = 3)

button_modulo = tk.Button(root, text = "%", command=lambda: intries("%"), width=6, height = 3, font=("Times New Roman", 13))
button_modulo.grid(row = 1, column = 1)

button_open = tk.Button(root, text = "(", command=lambda: intries("("), width=6, height = 3, font=("Times New Roman", 13))
button_open.grid(row = 1, column = 2)

button_close = tk.Button(root, text = ")", command=lambda: intries(")"), width=6, height = 3, font=("Times New Roman", 13))
button_close.grid(row = 1, column = 3)

button_equal = tk.Button(root, text = "=", command= math, width=6, height = 3, font=("Times New Roman", 13))
button_equal.grid(row = 5, column = 4)

button_clear = tk.Button(root, text = "C", command = reset, width=6, height = 3, font=("Times New Roman", 13))
button_clear.grid(row = 5, column = 1)

# Can be think as infinite loop in other language, but not quite. The function will call the tkinter event loop until user choose to terminate.
root.mainloop() 
