##################################### Functions ##########################################

""" The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using call by value (where the value is always an object reference, not the value of the object). 1 When a function calls another function, or calls itself recursively, a new local symbol table is created for that call """


def calculator(a, b, ops = ""):
	if (ops == ""):
		 return "Please Provide a operation you want to perform !!!!!"
	else:
		match ops:
			case "add":
				return a + b
			case "sub":
				return a - b
			case "mul":
				return a * b
			case "div":
				return a / b
			case "mod":
				return a % b			

print(calculator(5,6,"add"))
print(calculator(5,6,"mul"))
f = calculator(5,6)
print(f)
##################################### Functions ##########################################
