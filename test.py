print ('hello world')


name = 'Leon'



pattern = '{movie} + {name} + {rating}'
number = 110

result = pattern.format(movie=name, name=pattern, rating=number)

print(result)

man = '{} + {}'

apperresult = man.format(name, number+1) 

print(apperresult)

name = '{apperresult}' 
result = name.format(apperresult=name)

print(result)
