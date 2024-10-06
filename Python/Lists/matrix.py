n = int(input("Enter size of matrix 1: "))
matrix = []
for i in range(n):
    a, b, c = input("Enter three space separated values : ").split() 
    #split() creates a list of substrings
    l = [a, b, c]
    matrix.append(l)  
print(matrix)



n = int(input("Enter size of matrix 2: "))
matrix = []
for i in range(n):
    a, b, c = input("Enter three space separated values : ").split()
    a, b, c = int(a), int(b), int(c)
    l = [a, b, c]
    matrix.append(l)
print(matrix)



n = int(input("Enter size of matrix 3: "))
matrix = []
for i in range(n):
    print(f'Enter elements of row {i+1} and press enter after each element: ')
    a, b, c = input(), input(), input()
    l = [a, b, c]
    matrix.append(l) 
print(matrix)



n = int(input("Enter size of matrix 4: "))

matrix = [ ]
for i in range(n):
    L = [ ]
    for num in input("Enter three space separated values: ").split(' '):
        L.append(int(num))
    matrix.append(L)
print(matrix)