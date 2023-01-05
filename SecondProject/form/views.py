from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

# View for Get And Post Method Learning
def getPostMethod(request):
	if request.method == 'POST':
		name = request.POST['Employee_name']
		print("Name : "+name)
		try:
			gender = request.POST['E_Gender']
		except:
			print("You have Not Selected Your Gender")
		else:
			print("Gender : "+gender)
		finally:		
			dob = request.POST['Date_Of_Birth']
			print("DOB : "+dob)
			email = request.POST['Email_Id']
			print("Email ID : "+email)
			yoe = request.POST['Year_Of_Experience']
			print("Year's Of Experience : "+yoe)
			mob = request.POST['Mobile_Number']
			print("Mobile Number : "+mob)
			salary = request.POST['Salary']
			print("Salary : "+salary)

	return render(request, 'Request/home.html')

# View for Layout Design
def layout(request):
    return render(request, 'Layout/layout.html')

# global List to store data list
e_list = []
# count_id for assigning number to lists
c_id = 0

# View for Create ,Read, Update and Delete Operation
def crudoperation(request):
	global c_id 
	
	# if request is POST
	if request.method == "POST":
		# to check whether to insert or perform action (Edit and Delete)
		e_data = request.POST.values()         # store data into e_data variable
		e_data = list(e_data)				   # convert it into list								
		id = e_data[1]                         # store id into varaible 
		
		# if id is empty then insert employee record
		if id == "":
			# all values in POST Request
			e_data = request.POST.values()
			# make it list
			e_data = list(e_data)
			# add count_id as hidden value of every data list
			e_data[1] = c_id
			# increment count id by 1
			c_id = c_id + 1
			# append that into e_list
			e_list.append(e_data)
			# pass e_list into context as dictionary
			context = {
				'e_list' : e_list
			}
			return render(request, 'CRUD/home.html', context)
		
		# if id has value then perform action => Edit or Delete	
		else:
			# to check whether to delete or update
			e_data = request.POST.values()       # store data into e_data
			e_data = list(e_data)                # convert it into list
			toDo = e_data[2]                     # store value of e_data at 2nd Postion

			# if toDo ==> del then Employee record will be deleted
			if toDo == "del":
				e_data = request.POST.values()   # store data into e_data
				e_data = list(e_data)            # convert it into list
				# store value of e_data at 1st Position in id So that we get to know from e_list which list should be removed
				id = int(e_data[1])               
				# remove the list at (id) index from e_list
				e_list.pop(id)
				# pass e_list into context as dictionary
				context = {
					'e_list': e_list 
				}
				# decrement id counter by 1, bcz we delete the list from e_list so, size should be decrease
				c_id = c_id - 1
				return render(request, 'CRUD/home.html', context)

			# if toDo != > del then Employee record will be Edited
			else:
				e_data = request.POST.values()    # store data into e_data
				e_data = list(e_data)             # convert it into list
				# store value of e_data at 8th Postion into id to target that, In e_list which list values should be updated 
				id = int(e_data[8])
				# store new data 
				naya_data = e_data
				# Update Values
				e_list[id][2] = naya_data[1]
				e_list[id][3] = naya_data[2]
				e_list[id][4] = naya_data[3]
				e_list[id][5] = naya_data[4]
				e_list[id][6] = naya_data[5]
				e_list[id][7] = naya_data[6]
				e_list[id][8] = naya_data[7]
				# pass e_list into context as dictionary
				context = {
					'e_list': e_list 
				}
				return render(request, 'CRUD/home.html', context)	
	
	# if request is GET
	return render(request, 'CRUD/home.html')
	

