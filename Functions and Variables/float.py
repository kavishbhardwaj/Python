#Float is real number; its a data type similar to int or string

x = float(input("What's x?"))  #enter decimal point
y = float(input("What's y?"))

# https://docs.python.org/3/library/functions.html#round
z = round(x+y)
print(f"{z:,}")  #formatting numbers

z= x/y
print(z)

z = round(x/y , 2)
print(z)

z = x/y
print(f"{z:0.3f}")