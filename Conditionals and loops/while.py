'''
Keep accepting integers as input from the user until the user enters a negative number. 
Print the maximum among the positive numbers entered by the user. 
Print 0 if the user doesn't enter any positive integer
'''

# Initialize
num = int(input())
max_num = 0
# Loop
while num >= 0:
    if num > max_num:
        max_num = num
    num = int(input())
# Print output
print(max_num)


