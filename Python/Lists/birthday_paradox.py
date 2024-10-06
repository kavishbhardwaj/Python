import random

l = []

for i in range(50):
    l.append(random.randint(1,365))
print(l)


print(l.sort())
l.sort()
print(l)

l.sort(reverse = True)
print((l))

m =sorted(l)  
print(m)
print(len(m))

i = 0
flag = 0
while i<=len(m)-2:
    if m[i] == m[i+1]:
        print("Repeats", l[i])
        flag = 1
        break
    i  = i+1

if flag == 0:
    print("Doesn't repeat")