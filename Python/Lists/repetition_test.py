m = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8]
k = []

i = 0
flag = 0
while i<len(m)-1:
    if m[i] == m[i+1]:
        k.append(m[i])
        flag = 1
    i  = i+1

if flag == 0:
    print("Doesn't repeat")
if flag == 1:
    print("Repeates: ", k)