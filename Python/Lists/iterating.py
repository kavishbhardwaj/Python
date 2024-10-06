# Method-1
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num, end = " ")
print()


# Method-2
numbers = [1, 2, 3, 4]
index = 0
while index < len(numbers):
    print(numbers[index], end = " ")
    index += 1
print()

# Method-3
numbers = [1, 2, 3, 4]
for index in range(len(numbers)):
    print(numbers[index], end = " ")