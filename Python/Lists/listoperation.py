l = [1,2,3,4,5]
print("The list is: ", l)
print("Second element of list is: ", l[1])
a, b, c, d, e = l
print("First three elements of list are: ", a, b, c) 

l.append(2)    #repetition is allowed
print("Appended list", l)

l = l + [2]
print("Concatenated list: ", l)

l.remove(2)   #removes first occurence
print("List after removal of first occurence of '2': ", l)

m = []       #empty list
n = list()   #empty list
m.append(l)
n.append(l)
print("List of list: ", m)
print("List of list: ", n)

print(m[0][2])

print(f'Sum: {sum(l)}, Min: {min(l)}, Max: {max(l)}, Sorted list: {sorted(l)}')

print("range(5): ", list(range(5)))
print("range(1,5): ", list(range(1,5)))
print("range(1,5,2): ", list(range(1,5,2)))


print(type(l))
print(isinstance(l, list))
print(f'The list l has {len(l)} elements in it')
print(l[0], l[1], l[2], l[3])
print(l[1 : 3])
print(l[-2])