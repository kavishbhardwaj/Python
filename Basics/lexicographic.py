# https://www.unicode.org/charts/          unicode charts  
# go to latin script, ascii code for english 

print(ord('a'), ord('b'))
print(ord('a'), ord('A'))

print('a' < 'b')

'''The first characters from the two strings are compared. 
If they differ this determines the outcome of the comparison
If they are equal, then the second character of both the strings are compared.
'''
print('good' > 'bad')
print('nine' < 'one' )
print('a' < 'ab' < 'abc' < 'b')

a = 'good'
b = 'very good'
present = a in b
print(present)
not_present = b in a
print(not_present)


#In Python, the backslash - \ - is called the escape character
print('India\'s capital is \t New Delhi \n Really?')


