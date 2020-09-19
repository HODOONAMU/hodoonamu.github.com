#f-string 방식
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. I am {family} {name}')

#.format 방식
print('a is {}'.format('a'))

print('a is {0}, {1}, {2}'.format('1', '2', '3'))
print('a is {2}, {1}, {0}'.format('1', '2', '3'))

print('My name is {0} {1}. I am {1} {0}'.format('Jun', 'Sakai'))