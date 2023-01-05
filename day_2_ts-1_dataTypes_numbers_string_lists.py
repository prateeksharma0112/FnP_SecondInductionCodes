###################### Numbers ######################

# addition, subtraction, multiplication, divison, remainder (int, float)
num1 = 2
num2 = 4.5
print(num1+num2)
print(10/3)  # this will return a float value
print(10//3) # floor divison will retuen integer value
print(50-40)
print(10%3) 

# Powers in Python
print(2*3)    # Multilpy
print(2**3)   # 2 ki power 3
print(8**2)   # 8 ki power 2
print(5**3)   # 5 ki power 5

""" In interactive mode, the last printed expression is assigned to the variable(_) . """

###################### Numbers ######################

############## Strings are Immutable ################
# Strings
print('1. Prateek Sharma \n2. Animesh \n3. Shhubhang')

# Raw Strings
print(r'1. Prateek Sharma \n2. Animesh \n3. Shhubhang')

# Multiple Lines
print("""\
	1. Prateek Kumar Sharma     2. Aman      3. Shubhang
	4. Sharad                   5. Animesh   6. Srinivas   """)

# String concatenation
f = 'Prat'
s = 'eek'
print(f+s)
print('Pra'+'t'+s+" Kumar"+' Sharma')

# String Multiplication
print(3*'Prateek')

# Indexing Of strings
word = "Prateek Kumar Sharma"
print(word[0])
print(word[2])
print(word[5])

# Slicing 
print(word[0:5])
print(word[:5])
print(word[0:11])
print(word[1:])

# out of range slice indexes are handled gracefully when used for slicing
print(word[2:50])
print(word[50:])

# String Length
word1 = "PrateekKumarSharmaSnimeshShubang"
print(len(word1))

############## Strings are Immutable ################

#####################  Lists ########################
"""
Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list 
of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. 
"""
sampleList = [1,2,3,4,"Prateek","Aman",7,8,9,"Shubang"]
print(sampleList)
print(sampleList[0])
print(sampleList[4])
print(sampleList[5])

# Slicing returns new Lists
print(sampleList[3:])
print(sampleList[3:7])
print(sampleList[2:9]) 

""" All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list """
# (A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original)
# (A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original)

# Lists also support operations like concatenation 

list2 = [1,2,34,6,77,88]
list3 = [8,9,9,88,56,345]
print(list2+list3)
print(list2 + ["Ok Working"])

# Lists are Mutable 
list4 = [10,20,30,50,60]
print(list4)
list4[3] = 40
print(list4)
list4[4] = 50
print(list4)
list4.append(60)
print(list4)
list4.append(700)
print(list4)

# Assignment to slices is also possible

# length
print(len(list4))
print(len(list3))
print(len(list2))
print(len(sampleList))

##### Nesting Of Lists ######

newlist = [list4,list3,list2]
print(newlist)
print(newlist[0])
print(newlist[1])
print(newlist[2])
newlist.append(["Great"])
print(newlist)

#####################  Lists ########################
