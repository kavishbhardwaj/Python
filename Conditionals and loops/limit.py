#train of square roots

import math
# sqrt(2 + sqrt(2 + sqrt(2 + ...) ))
x = 0
for n in range(1, 6):
    x = math.sqrt(2 + x)
    print(f'n = {n}, x_n = {x:.3f}')

x_prev, x_curr = 0, math.sqrt(2)
tol, count = 0.00001, 0
while abs(x_curr - x_prev) >= tol:
    x_prev = x_curr
    x_curr = math.sqrt(2 + x_prev)
    count += 1
print(f'Value of x at {tol} tolerance is {x_curr}')
print(f'It took {count} iterations')



# {sqrt(2)-1}^n
n = int(input("Enter number of iterations n: "))                # sequence length
CONST = math.pow(2, 0.5) - 1    # basic term in the sequence
a_n = 1                         # zeroth term
for i in range(n):
    a_n = a_n * CONST           # computing the nth term
print(a_n)


n = int(input("Find nth term for n: "))    # sequence length
x_n, y_n = -1, 1    # x_1 and y_1
for i in range(n - 1):
    x_n, y_n = 2 * y_n - x_n, x_n - y_n
print(x_n, y_n)
print("Value of root(2) is: ", -x_n/y_n)