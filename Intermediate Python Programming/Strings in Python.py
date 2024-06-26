first_name = "Sudhanshu"
last_name = 'Yadav'
location = str("Delhi")
#Case 1 Print values of strings
print("Case 1 Output . . .")
print(first_name)
print(last_name)
print(location)
#Case 2 Print data type of Variables
print("Case 2 Output . . .")
print(type(first_name))
print(type(last_name))
print(type(location))
#Case 3 String works like Collection
print("Case 3 Output . . .")
print(first_name[0])
for c in first_name:
    print(c)
#Case 4 Find length of string
print("Case 4 Output . . .")
print(len(first_name))
for i in range(len(first_name)):
    print(first_name[i])
#Case 5 Use of in & Not in String
print("Case 5 Output . . .")
print("Sud" in first_name)
print("Sud" not in first_name)
print("Yad" not in last_name)
print("Yad " in last_name)
#Case 6 Slicing Strings
print("Case 6 Output . . .")
print(first_name[1:5])
print(first_name[:5])
print(first_name[1:])
#Case 7 Modify Strings
print("Case 7 Output . . .")
n = "     Sud Yadav   "
print(first_name.upper())
print(first_name.lower())
print(n.strip())
print(n.replace("d","n"))
name = "My Name is Sudhanshu Yadav"
print(name.split(" "))
print(type(name.split(" ")))
words = name.split(" ")
print(words[1])
#Case 8 Strings are Immutable
print("Case 8 Output . . .")
c = "Sudhanshu"
print(id(c))            #Show the memory address of this variable c
c = "Sudhanshu Yadav"
print(id(c))            #Show the memory address of this variable c

#Case 9 Other Operations on Strings
print("Case 9 Output . . .")
print(c.capitalize())       #Only first letter will be in capitals
print(c.title())            #Print First letter is in capital
print(c.count("d"))         #Count Occurrence of D in string
h = "I am Sudhanshu And I Teach Python. Python is a very easy programming language"
print(h.find("Python"))          #Find Index of Python in the string
print(h.find("Java"))            #Find Index of string not present
#Case 10 String Comparison
print("Case 10 Output . . .")
name_1 = "Sudhanshu"
name_2 = "Sudhanshu"
name_3 = "Yadav"
name_4 = "sudhanshu"
print(name_1 == name_2)             #Check if Strings are equal or not
print(name_1 == name_3)             #Check if Strings are equal or not
print(name_1.__eq__(name_2))        #Check if Strings are equal or not
print(name_1.__eq__(name_3))        #Check if Strings are equal or not
print(name_1.__eq__(name_4))        #Check if Strings are equal or not
print(name_1.casefold()==name_4)    #Check if Strings are equal or not irrespective of Upper Case & Lower Case