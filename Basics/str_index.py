#A string is a sequence of characters. Sequences support indexing.

word = 'world'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])


print(word[-5])
print(word[-4])
print(word[-3])
print(word[-2])
print(word[-1])



email = 'CS_10_014@iitm.ac.in'
branch = email[0 : 2]
print(branch)
print(email[3 : 5])
print(email[6 : 9])
print(email[10 : 14])


in_roll = email[ : 9]
print(in_roll)



email = 'CS_10_014@iitm.ac.in'
domain = email[-10 : ]
print(domain)



word = 'world'
print(word[-4 : 3])
print(word[1 : -2])