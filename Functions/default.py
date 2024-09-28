def distance(x, y, metric = 'manhattan'):   #The parameter metric has 'manhattan' as the default value
    if metric == 'manhattan':
        return abs(x) + abs(y)
    elif metric == 'euclidean':
        return pow(x ** 2 + y ** 2, 0.5)
    

print("Manhatttan distance = ", distance(2, y = 3))   
#the keyword arguments must always come at the end


print("Euclidean distance = ", distance(y = 3, x = 2, metric = 'euclidean'))

#Default parameters always come at the end of the parameter list in a function definition