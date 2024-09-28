x = 1.0
avar = 'cool'
def foo():
    print(locals())
    y = 2.0
    print(locals())
    global z
    print(locals())
    # The moment control exits the function, the namespace corresponding to it is deleted

foo()
z = 10
print(globals())

''' 
How does the Python interpreter internally process these names? 
It uses a concept called namespaces.
A namespace can be thought of as a lookup table — dictionary to be precise — that maps names to objects
x, avar and foo are present in the namespace.
x and avar are mapped to the objects 1 and cool respectively, 
while foo is mapped to the location in the memory where the function's definition is stored
'''

print('x' in globals())
print('avar' in globals())
print('foo' in globals())
print('y' in globals())

'''
nothing prevents us from using the name of a built-in function, such as print, as the name of a variable. 
But this is a very bad practice that should be avoided at any cost because
if in-bulit function print can't be used in this situation
'''