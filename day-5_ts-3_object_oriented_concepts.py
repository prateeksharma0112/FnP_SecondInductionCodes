################################ Object Oriented Programming ##############################

# 1. Classes
""" Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state. """

# 2. Python Scopes and Namespaces
## 2.1 Namespaces
""" (*) A namespace is a mapping from names to objects.
	(*) A namespace is a collection of currently defined symbolic names along with information about the object that each name references.
	(*) Write modname.the_answer = 42. Writable attributes may also be deleted with the del statement. For example, del modname.the_answer will remove the attribute the_answer from the object named by modname.
	(*) Three types of namespace global, local and built-in.
"""
## 2.2 Scopes
""" (*) A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.
	(*) Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

		=>	the innermost scope, which is searched first, contains the local names

		=>	the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names

		=>	the next-to-last scope contains the current module’s global names

		=>	the outermost scope (searched last) is the namespace containing built-in names
			
	(*) Assignments do not copy data — they just bind names to objects.	
"""
# 3. Class Definition
"""
	class ClassName:
		<Statement 1>
		<Statement 2>
		
		<Statement N>
"""
## 3.1 Class Objects
""" Class objects support two kinds of operations: attribute references and instantiation.
"""
## 3.2 Instance Objects
""" The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.
"""
## 3.3 Method Objects
""" 
"""
## 3.4 Class and Instance Variables
## 3.5 Random Remarks

# Code implementation

class studentData:
	pass
# creating an object
s1 = studentData
s2 = studentData
s3 = studentData

s1.name = "Prateek"   # class variable
s1.age = 23			  # class variable
s1.marks = 100		  # class variable

s2.name = "Aman"
s2.age = 22
s2.marks = 95

print(s1)
print(s1.name, s1.age, s1.marks)	# Aman, 22, 95
print(s2.name, s2.age, s2.marks)	# Aman, 22, 95
print(s3.name, s3.age, s3.marks)	# Aman, 22, 95





















################################ Object Oriented Programming ############################
