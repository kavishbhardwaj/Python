#This program introduces numerical data type "integer" and functions

'''x += a	x = x + a
x -= a	x = x - a
x *= a	x = x * a
x /= a	x = x / a
x %= a	x = x % a
x **= a	x = x ** a'''

x, y = 1, 2
print(x, y)
print('The type of x is', type(x))

x = input("what's x ?")
y = input("What's y ?")

z = x+y
print("concatenation", z)

#type conversion #int function will convert input to integer type
z = int(x) \
    + int(y)       # int is not only a data type but also a function
print("No, the correct sum of inetegers is", z)

'''
#round() accepts a number as input and returns integer closest to it
#abs() accepts a number as input and returns its absolute value
int() - If an integer enclosed within quotes is entered as input, then the output is that integer. int('123') is 123. 
If a float is entered as input, then the decimal part is thrown away and the integer part is returned. int(1.2) returns 1
If a float is passed in the form of a string, a ValueError will be thrown- int('2.5')
isinstance() is used to check if an object is of a specified type. 
For example isinstance(3, int) returns the value True as the literal 3 is of type int
pow(x, y, z) gives the remainder when x^y is divided by z
pow(x, y) returns the value of x^y or x**y
https://docs.python.org/3/library/functions.html
'''

x = int(input("what's x again?"))  #nesting of functions
y = int(input("What's y again?"))

print(x+y)

print("sum", int(input("What's x ?"))+int(input("What's y ?")))      #nesting of functions

z = x/y
print("Division", z)

z = x % y #Modulo
print("Remainder", z)

z1 = x//y   #floor division
z2 = x**y
print('floor division {}; exponentiation {}'.format(z1, z2))
