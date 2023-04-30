# this is a comment in python and the following lines declare variables and print them
name = 'João Felipe Zini'
print('Olá,', name, 'seja bem-vindo!')

person = 'João'
print('Olá,', person)

number = 1
number += 2
print(number)

# first loop for in python

paradigm = 5

lesserArr = []
greaterArr = []

for i in range(10):
    if (i < paradigm):
        lesserArr.append(i)
    elif (i > paradigm):
        greaterArr.append(i)

print('Final result:')
print('This is the lesserArr', lesserArr)
print('This is the greaterArr', greaterArr)
