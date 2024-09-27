#minimum positive integer x such that (x**2 + x + 41) is divisible by 41

z = 40
x = 1
while z % 41 != 0:
    z = x**2 + x + 41
    x = x + 1
print(x-1)






