#minimum positive integer x such that (x**2 + x + 41) is divisible by 41

z = 40
x = 1
while z % 41 != 0:
    z = x**2 + x + 41
    x = x + 1
print(x-1)


# prints all positive integers less than or equal to 50 that are divisible by 3
x = 0
print("Multiples of three <= 50", end = ': ')
while x < 50:
    x = x + 1
    if x % 3 != 0:
        continue
    print(x, end = ',')

print()  #newline

#prints the smallest positive integer that is divisible by 2, 3 and 4
num = 1
while True:
    if (num % 2 == 0) and (num % 3 == 0) and (num % 4 == 0):
        break
    num = num + 1
print("LCM of 2,3,4 is", num)
print()

#use of sep and end 
n = int(input("Integer in multiple of 3: "))
print('|', end = '')
for i in range(1, n + 1, 3):
    print(i, i + 1, i + 2, sep = ',', end = '|')


#how many times break gets executed
for i in range(10):
    for j in range(10):
        print(f'j = {j}')
        break
    print(f'i = {i}')
    break