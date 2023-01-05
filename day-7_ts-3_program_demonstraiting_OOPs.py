######################################################################## Program demonstrating Object oriented and data structure ################################################################################
# Base Class schoolMember
class schoolMember:
	
	# class variable
	total_members = 0
	database = []
	
	# constructor function
	def __init__(self, name, age):
		# instance variable
		self.name = name
		self.age = age
		self.is_active = True
		schoolMember.total_members += 1
		schoolMember.database.append(self)
	# instance method	
	def introduce(self):
		print(self.name,"has Joined !!!!!")
		print("My Name Is",self.name,"I am",self.age,"Years Old.")
		
	def members(self):
		print("Total School Members In School including (Teacher and Student) Is",schoolMember.total_members)
	
	def remove(self):
		if self.is_active:
			print(self.name," Has Leave our School. All the Best For Future !!!!!")
			schoolMember.total_members -= 1
			self.is_active = False
		else:
			print(self.name,"Has Already Leave Our School")	
	
	def __repr__(self):
		return "[Name: {}, Age: {}, Active Member: {}]".format(self.name, self.age, self.is_active)	# Returns a string as a representation of the object.

#******* INHERITANCE ********# derived class from Base class (schoolMember)
class student(schoolMember):
	
	# constructor function
	def __init__(self, name, age, my_class, roll_no):
		super().__init__(name, age)  # it will call constructor of base class (for reusability of code)
		
		# additional properties
		self.my_class = my_class
		self.roll_no = roll_no
	
	# instance method (polymorphism, it will override with base class function)
	def introduce(self):
		print("New Student",self.name,"has Joined Our School.")
		print(self.name,"Will study in",self.my_class,"Class.","and Roll Number Is",self.roll_no)

#******* INHERITANCE ********#		
class teacher(schoolMember):
	
	# constructor function
	def __init__(self, name, age, subject, salary):
		super().__init__(name, age)   # it will call constructor of base class (for reusability of code)	
		
		# additional properties
		self.subject = subject
		self.salary = salary
		
	# instance method (polymorphism, it will override with base class function)
	def introduce(self):
		print(self.name," has Joined our School as a Teacher")
		print(self.name,"Will Teach",self.subject,"subject.","and Salary is",self.salary)
		
########### Object Creation and Deletion ############		
m1 = schoolMember("Prateek Kumar Sharma", 22)   # add new member => M1
m1.introduce()
m1.members()
print("School Database : ", schoolMember.database)

print()
s1 = student("Aman", 24, 12, 51455102718)       # add new student => S1
s1.introduce()
s1.members()
print("School Database : ", schoolMember.database)

print()
t1 = teacher("Shubhang", 24, "Data Science", "12 LPA")	# add new teacher => T1
t1.introduce()
t1.members()
print("School Database : ", schoolMember.database)

print() # To remove a teacher => T1 if he is a active member for school, count will reduce by 1
t1.remove()      # To remove a teacher => T1
t1.members()     
print("School Database : ", schoolMember.database)  # but in main database of school, record will be  always save 
		
print()
t1.remove()   # if we again try to remove then it will not work because it has already leave school
t1.members()  # not reflect in members number as well
print("School Database : ", schoolMember.database)   # but in main database of school, record will be  always save 
 
print()
s2 = student("Saransh", 25, 10, 51555102718)  # add new student => S2
s2.introduce()
s2.members()
print("School Database : ", schoolMember.database)

print()
s1.remove()      # To remove a student => S1 
s1.members()     # count will reduce by 1  
print("School Database : ", schoolMember.database)  

print()
t2 = teacher("Sharad", 30, "Data Science", "22 LPA")	 # adding new teacher T2 	
t2.introduce()
t2.members()
print("School Database : ", schoolMember.database)
