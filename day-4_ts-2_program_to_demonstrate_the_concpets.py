################################## write a python program to demonstrate the concepts of data types, variables, loops, control flow and functions #######################################

""" this a basic calculator to perform basic operations like addition, subtraction, modulus, division, multiply  """

# funtion defintion
def calculator (num1,num2,operation):
# this is a calculator function on the basis of given input num1,num2 and operator it will return a output.
	if   operation == "+": 
		return num1 + num2  	# if operation = '+' => it will return sum of two numbers.
	elif operation == "-":
		return num1 - num2		# if operation = '-' => it will return subtraction of two numbers.
	elif operation == "*":
		return num1 * num2		# if operation = '*' => it will return multiplication of two numbers.
	elif operation == "/":		
		return num1 / num2		# if operation = '/' => it will return division of two numbers.
	elif operation == "%":			
		return num1 % num2		# if operation = '%' => it will return modulus of two numbers.
	else:
		return					# if operation = '' or an other value => it will return None.

# funtion defintion
def takeInputandPrintOutput():
#   this is function which take inputs and print the calculated output.
	value1 = float(input("Enter First Number: "))  # It will take integer value as input and stored in value1(variable).
	value2 = float(input("Enter Second Number: ")) # It will take integer value as input and stored in value2(variable).
	operation = str(input("""	For Addition Press:       +	     
	For Subtraction Press:    -
	For Multiplication Press: *
	For Division Press:       /
	For Remainder Press:      %   
	Which Operation you want to Perform: """)) 	 # It will take string as input and stored in operation(variable).
	
	# call the calculator function to calculate the result and stored into a variable.
	calculated_result = calculator(value1,value2,operation)
	
	# print the output
	if calculated_result == None:
		print("You have not Enter an Valid Operation To Perform")  # If  calculated_result == None => then, print the message that not enter valid operator.
	else:	
		print("The Output For the Given Input values and Operation Is:", calculated_result,'\n')   # else => print the calculated output.
	
	# Ask user If they want to use calculator again.
	do_more = str(input("Do you Want to Performe Calculation again?? if Yes type\'Y' or if No type\'N' : ")) # do_more is a variable which store input as string provided by users.
	
	if do_more == "Y":         
		takeInputandPrintOutput()  # If do_more value = "Y" => then again called the takeInputandPrintOutput(), recursive Call.
	else:			
		print("Calculator Stopped !!!!!!!!!!!!!!!")  # If do_more value = "N" => then simply print the message "Calculation Stopped" and the program get stop.

# Function Call to run calculator for the first time.
takeInputandPrintOutput()	
			  
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX write a python program to demonstrate the concepts of data types, variables, loops, control flow and functions XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
