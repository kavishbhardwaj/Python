#This program introduces to string data type and functions

#Ask user for their name
#print is a function and its arguements/parameters are inside the brackets
print("What's your name ? ")                                                               
name = input()              #result of input function is assigned to variable "name"  
name = f' Respected {name}'  
#print(*objects, sep=' ', end='\n', file=None, flush=False)   
# #end of the line will be nothing whereas in original syntax its \n                           
print("Hello, \"dear\" 'user' ", name, end = "")       #quotation mark inside a string 


#Ask user for their name again
print("Can you tell your full name again ?", end ="039  ")
# https://docs.python.org/3/library/stdtypes.html#string-methods 
# title function and strip function are methods here
first_name, last_name = input().strip().title().split(" ")                     # strip away blank spaces and capitalise
print(f"Hello, {name}", first_name, end = "\n")                                #F string makes it possible to enter variable inside quotes


#Ask user for their friend's name
friend_name = input("What's your best friend's name ?").strip().title()
print("Say Hello to " + friend_name)


valid = name.isalpha()
print(valid)
'''name.isalpha() returns a boolean value. 
If every character in the string is an alphabet and 
the string is non-empty, it returns True, and False otherwise

https://docs.python.org/3/library/stdtypes.html#string-methods
'''

"""
https://docs.python.org/3/library/functions.html
"""

#in python both single and double quotes can be used provided end and start is by the same type


#how to write in multiple lines without writing hash before every line
'''interactive python mode- not needed to save a .py file; 
type python in terminal window and three arrows appear; 
any line of code is interpreted immediately;
use exit() or ctrl+z+enter to exit'''

