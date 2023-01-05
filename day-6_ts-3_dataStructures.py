# Python -In-Built Data Structures

# Data Structures => techniques of storing data in RAM or memory

################################################################################################# 1. Lists ####################################################################################################
"""
	Ordered / Sequence collection of elements
	Indexable
	Mutable
	Hetrogenous Elements
"""
print("############ LISTS #############")
# Create list
my_list = [6,4,5,6,7,8,9,90]

print(my_list)
print(type(my_list))

# Indexing/Slicing of lists

print(my_list[0])
print(my_list[-1]) 
print(my_list[1:-1])


# Mutable Property
my_list[0] = 99

print(my_list)

######## Important functions in Lists ##########

# append at last
my_list.append(1000)
print(my_list)

# insert at indexed element
my_list.insert(2,2000)
print(my_list)

# delete last element
my_list.pop()
print(my_list)

# delete indexed element
my_list.pop(0)
print(my_list)

# reverse
my_list.reverse()
print(my_list)

# sorting
my_list.sort()
print(my_list)

# in operator
print(90 in my_list)
print(1 in my_list)

# iterartion
for ele in my_list:
	print(ele*2)

### List Comprehension ###
print("List Comprehension") 
print(my_list)

new_list = [ele*2 for ele in my_list]
print(new_list)

# Hetrogenous List
print("Hetrogenous List")
my_list2 = ["I","m","Prateek",True,"Age:",22,[0,1,2]]
print(my_list2)

# 2D - List
print("2D - List")
list_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2d)
print(list_2d[1][0])  # => 4


################################################################################################# 2. Tuples ####################################################################################################

# we use tuples where data is sensitive when we want no - one will change the data
############### Tuples are Faster Than List #################
"""
	similar to list but READ ONLY
	ordered, collection of Items
	Indexable
	Immutable
"""
print()
print("############ TUPLES #############")
## create tuple

tup = (8,9,"HELLO",True)
print(tup)
print(type(tup))
print(tup[0])
print(tup[-1])

# Iterartion
for i in tup:
	print(i)

################################################################################################# 3. Sets ######################################################################################################

"""
	Contain only Unique Elements
	Mutable
	Un-Ordered
	Un-Indexable
"""
print()
print("############## SETS ################# ")

# Create set

my_set = {9,4,5,5,4,3,5,6,7,8,9,7,9,3,4,6}
print(my_set)
print(type(my_set))

## remove element from Set
my_set.remove(6)
print(my_set)

############################################################################################### 4. Dictionary ##################################################################################################
"""
	Stores data in (key-value) pair form. TABULAR FORM (In C++ => HashMap)
	Unordered
	UnIndexable
	acess the values, with the help of key
"""
print()
print("############## Dictionary #################")

# create Dictionary

user_info = {
	"name" : "Prateek K Sharma",
	"age"  : 34,
	"Nationality" : "Indian" ,
}
print(user_info)
print(type(user_info))

# acessing Elements
print(user_info["name"])

# add Data into Dictionary
user_info["hobby"] = ["Singing", "Cricket", "Coding"]

print(user_info)

# Display all Keys
print(user_info.keys())

# Display All Values
print(user_info.values())

# Display key, values in pair in tuples
print(user_info.items())

# Delete Key, Values 
user_info.pop("hobby")
print(user_info)













