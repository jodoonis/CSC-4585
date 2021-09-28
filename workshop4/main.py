
op = 0
in_ = 0
x = 0
y = 0
exit = False

def inputNumber(prompt):
  while True:
    try:
       userInput = float(input(prompt))
    except ValueError:
       print("Invailid input: Please enter an valid number.\n")
       continue
    else:
       return userInput 
       break 


def inputMenu(prompt):
  while True:
    try:
       userInput = int(input(prompt))
    except ValueError:
       print("Invailid input.")
       continue
    else:
       return userInput 
       break 


while exit == False:
	print("Select from the options below:\n\tEnter '1' for multiplication.\n\tEnter '2' for division.\n\tEnter '3' to Exit.")
	op = inputMenu("Menu selection: ")
	op = int(op)
	print("")

	if op == 1:
		in_ = inputNumber("Enter your first number: ")
		x = in_
		in_ = inputNumber("Enter your second number: ")
		y = in_

		ans = x * y
		print("Product: ", ans, "\n")

	elif op == 2:
		in_ = inputNumber("Enter your first number: ")
		x = in_
		in_ = inputNumber("Enter your second number: ")
		y = in_

		if y == 0:
			print("Undefined\n")
			continue

		ans = x / y
		print("Quotient: ", ans, "\n")

	elif op == 3:
		print("Exitting program...")
		exit = True

	else:
		print("Invailid selection...\n")
