x = int(input("Enter the value of x ? "))
y = int(input("Enter the value of y ? "))
z = int(input("Enter value of z ? "))


if x == y or x == z or y == z:        # or
    if y != z:
        if y<z:             #can be written as  x == y < z in python
            print("x = y < z")
        else:
            print("x = y > z")

    elif z != y:                        #not equal to !=
        if z<y:
            print("x = z < y")
        else:
            print("x = z > y")

    elif z != x:
        if z<x:
            print("x < y = z")
        else:
            print("x > y = z")

    else:
        print("x = y = z")

else: 
    if x<y and y<z:                      #can be written as x < y < z in python
        print("x < y < z")

    elif x<z<y:
        print("x < z < y")

    elif z<x<y:
        print("z < x < y")

    elif z<y<x:
        print("z < y < x")

    elif y<x<z:
        print("y < x < z")

    else:
        print("y < z < x")


