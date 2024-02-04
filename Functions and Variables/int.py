#This program introduces numerical data type "integer" and functions

x = input("what's x ?")
y = input("What's y ?")

z = x+y
print("concatenation", z)

z = int(x) + int(y)       # int is not only a data type but also a function
print("No, the correct sum of inetegers is", z)

x = int(input("what's x again?"))  #nesting of functions
y = int(input("What's y again?"))

print(x+y)

print(int(input("What's x ?"))+int(input("What's y ?")))      #nesting of functions

z = x/y
print("Division", z)


z= x//y   #floor division
print("floor division", z)