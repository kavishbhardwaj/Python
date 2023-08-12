#This program introduces to string data type and functions

#Ask user for their name
#print is a function and its arguements/parameters are inside the brackets
print("What's your name ? ")                                                               
name = input()              #result of input function is assigned to variable "name"    
#print(*objects, sep=' ', end='\n', file=None, flush=False)   
# #end of the line will be nothing whereas in original syntax its \n                           
print("Hello, \"dear\" 'user' ", name, end = "")  


#Ask user for their name again
print("Can you tell your name again ?", end ="039  ")
# https://docs.python.org/3/library/stdtypes.html#string-methods 
# title function and strip function are methods here
first_name, last_name = input().strip().title().split(" ")                     # strip away blank spaces and capitalise
print(f"Hello, {name}", first_name, end = "\n")                                #F string makes it possible to enter varable inside quotes


#Ask user for their friend's name
friend_name = input("What's your best friend's name ?").strip().title()
print("Say Hello to " + friend_name)

"""
https://docs.python.org/3/library/functions.html
"""

#in python both single and double quotes can be used provided end and start is by the same type

#interactive python mode- not needed to save a .py file; type python in terminal window and three arrows appear; any line of code is interpreted immediately