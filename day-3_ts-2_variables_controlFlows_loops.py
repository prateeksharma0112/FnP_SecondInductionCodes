########################### Variables ############################

print() # this will print new line because it will pass an empty value as an arguement so it print empty and come to next line
# variable creation and assignment of value
a = 10
print(a)
a = 20
print(a)
A = "Capital A"
print(A)
print(a,A)
a, A = "Small A","Capital A"
print(a,A)
a,b,c,d,e,f,g = 1,2,3,4,5,6,7
print(a,b,c,d,e,f,g)

########################### Variables ############################

########################### Control Flows ########################

# ************** if - else Statements ***************** 
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if a>b:
    print("The Addition For Two Number Is:",a+b)
else:
    print("The Subtraction For the Two Number Is:",b-a)	

# ********** if - elif - elif -..... - else ************
a = int(input("Enter Your Marks To Check Your Percentage Range & Grade: "))

if a >= 0 and a <= 10:
	print("Your Percentage Is In The Range Of 0 to 10", "Work Hard, You are Fail !!!!!")
elif a <= 20:
	print("Your Percentage Is In The Range Of 11 to 20","Work Hard, You are Fail !!!!!")
elif a <= 30:
	print("Your Percentage Is In The Range Of 21 to 30","Work Hard, You are Fail !!!!!")
elif a <= 40:
	print("Your Percentage Is In The Range Of 31 to 40","Grade: C+")
elif a <= 50:
	print("Your Percentage Is In The Range Of 41 to 50","Grade: B")
elif a <= 60:
	print("Your Percentage Is In The Range Of 51 to 60","Grade: B+")
elif a <= 70:
	print("Your Percentage Is In The Range Of 61 to 70","Grade: A")
elif a <= 80:
	print("Your Percentage Is In The Range Of 71 to 80","Grade: A+")
elif a <= 90:
	print("Your Percentage Is In The Range Of 81 to 90","Grade: O")								
elif a <= 100:
	print("Your Percentage Is In The Range Of 91 to 100","Grade: O+")
else:
	print("Please Enter Valid Number Between the Range Of 0 to 100")	
########################### Control Flows ########################

########################### Loops ################################

### For statements ###

numbers = [0,1,2,3,4,5,6,7,8,9,10]
for i in numbers:
	print(i)

for i in range(10):     # print from 0 to 9
	print(i)
for i in range(10,21):  # print from 10 ...to... 20
	print(i)
for i in range(0,21,2): # print from 0 to 20 with a diffrence of 2 like 0,2,4,6....20
	print(i)   
	
namelist = ["Prateek", "Aman", "Animesh", "Shubhang", "Sharad"]
for i in range(len(namelist)):
	print(i,namelist[i])

print(sum(range(5))) # 0+1+2+3+4 => 10

#### break and continue Statements, and else Clauses on Loops #####
""" Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. """


## break
for i in range(20,40):
	if i % 2 == 0 :
		print(i,"is even Number.")
	else:
		print("Break Executed")
		break # come out of the innermost loop
## continue
for i in range(10):
	if i % 2 == 0 :
		print(i,"is even Number.")
	else:
		print("Continue Executed")
		continue    # move to iterator

## pass

for i in range(10):
	if i % 2 == 0 :
		print(i,"is even Number.")
		
	else:
		pass  # it simply ignore that part
		print(i,"Pass Executed")

## match statements

num1 = int(input("Enter a Number Between 0 to 5: "))
match num1:
	case 0:
		print("You got a Lottery")
	case 1:
		print("You are too close")
	case 2:
		print("You won Amazon Voucher")
	case 3:
		print("You won 100rs")
	case 4:
		print("Better Luck Next Time!!!")				
	case 5:
		print("You got a Lottery")
	case _:
		print("OOPS, Please Enter a Valid Number !!!!!!!!!!!")

########################### Loops ################################
