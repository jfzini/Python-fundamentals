# this is a comment in python and the following lines
# declare variables and print them

name = 'João Felipe Zini'
print('Olá,', name, 'seja bem-vindo!')

person = 'João'
print('Olá,', person)

number = 1
number += 2
print(number)

# first loop for in python

paradigm = 5

# in python, the best practice is to use snake_case
lesser_arr = []
greater_arr = []

for i in range(10):
    if (i < paradigm):
        lesser_arr.append(i)
    elif (i > paradigm):
        greater_arr.append(i)

print('Final result:')
print('This is the lesserArr', lesser_arr)
print('This is the greaterArr', greater_arr)
