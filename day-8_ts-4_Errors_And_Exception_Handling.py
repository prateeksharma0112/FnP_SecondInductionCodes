#################################################### Errors #############################################################


###################################### Exception and Exception Handling #################################################
print("\n")
print("First Program Started to understand the Flow in try and Except")
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

try:
	print("*************** You have Enetered into the Try BLOCK **************")
	result = a / b
	print("The divsion of Two Number Is : ",result)
except Exception:
	print("*********** You have Entered into the Exception Block **************")
	print("Number Cannot be Divided By",0,"Please enter the values Again")

print ("Good Bye !!!")  
print("\n")
##########################################################################################################################

print("Second Program Started to understand the try and Except\n")
try:
	a = int(input("Enter First Number : "))
	b = int(input("Enter Second Number : "))
	result = a / b
	print("The divsion of Two Number Is : ",result,"\n")
	
except Exception as p:
	print("This error Has Occured : ", p,"\n")

print ("********** Good Bye ***********")
print("\n")
##########################################################################################################################

print("Hi, Prateek All The Best For Today's Task i.e Exception Handling (try, except, else, finally) \n")
try:
	print("************ Program Has Started ***************")
	a = int(input("Enter First Number : "))
	b = int(input("Enter Second Number : "))
	result = a / b

except KeyboardInterrupt:
	print("\nYour Keyboard Has Interrupted")

except Exception as p:
	print("This error Has Occured : ", p)

else:
	print("The divsion of Two Number Is : ",result)

finally:
	print("!!!!!!!!!!!! Program Has Stopped !!!!!!!!!!!!!!!")

print ("********** Good Bye ***********")
print("\n")
##########################################################################################################################

print("Learn To Raise Exception")
try:
	raise NameError         # forcefully raise exception

except NameError:
	print("Ok")
print("\n")
##########################################################################################################################
######################################### Custom Exception and Raise Exception ###########################################

print("Learn To Make Custom Exception \n")
class mySampleException(Exception):
	# custom Exception
	def __init__(self, data):
			self.data = data
			
	def __repr__(self):
		return self.data

try:
	raise mySampleException("Your Custom Exception Runs SucessFully !!!")
except mySampleException as m:
	print("STATUS ==> ",m)
