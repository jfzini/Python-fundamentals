# this is a comment in python and the following lines
# declare variables and print them

# name = 'João Felipe Zini'
# print('Olá,', name, 'seja bem-vindo!')

# person = 'João'
# print('Olá,', person)

# number = 1
# number += 2
# print(number)

# first loop for in python

# paradigm = 5

# print(paradigm == 5)

# in python, the best practice is to use snake_case
# lesser_arr = []
# greater_arr = []

# for i in range(10):
#     if (i < paradigm):
#         lesser_arr.append(i)
#     elif (i > paradigm):
#         greater_arr.append(i)

# print('Final result:')
# print('This is the lesserArr', lesser_arr)
# print('This is the greaterArr', greater_arr)
# print(type(paradigm))

some_number = 73
# print(some_number == 10)
# print(some_number < 5)
# print(some_number < 15)
# print(5 < some_number < 15)
# print(5 < some_number and some_number < 15)

some_bool = False
some_list = [10, 11, 12, 13, 14, 15]

# print(not some_bool)

some_string = 'brasilia'

# print('brasil' in some_string)
# print('Brasil' in some_string)
# print('bresil' in some_string)
# print('bresil' not in some_string)
# print(len(some_string))
# print(some_string.upper())
# print(some_string.lower())
# print(some_string.title())
# print('Brasil' in some_string.title())

# print(some_string.startswith('bras'))
# print(some_string.endswith('ilia'))
# print(some_string.find('ilia'))
# print(some_list.find(12)) find is not an array method
# print(some_string.split(''))

print(some_string + ' tem ' + str(some_number) + ' anos')
print(str(some_number))
print(type(some_number))  # str() doesnt change the type of the original var
print(bool(some_number))
print(float(some_number))

# f'' corresponds to template literals
print(f'{some_string} tem {some_number} anos')

some_float = 11.212223654

# similar to toFixed, but apparently only work with f str
print(f'{some_float:.2f}')
