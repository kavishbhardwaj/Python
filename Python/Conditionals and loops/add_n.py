import time
start_time = time.time()
n = 150000000
total = 0
for i in range(1, n+1):
    total = total + i 

print(total) 
end_time = time.time()  # End time tracking
print(f"Execution time: {end_time - start_time} seconds")