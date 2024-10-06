for i in range(5):
    print(i)

for i in range(10, 100):
    print(i)

for i in range(10, 100, 2):
    print(i)

for i in range(98, 9, -2):
    print(i)

#empty sequence
for i in range(10, 5):
    print(i)

#for i in range(0.0, 10.0):
# wrong code floats are not allowed  


total = 0
for i in range(1, 5):    
    print(f'i = {i}')
    for j in range(i): 
        print(f'j = {j}')       
        total = total + i
        print(f'total = {total}')
print(total)  