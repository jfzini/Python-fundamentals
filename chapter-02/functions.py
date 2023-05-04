# from control import arr
# import activities as act
import itertools
import random


def sum(a, b):
    return a + b


# print(sum(4, 5))


def highest_number(list):
    max_number = max(list)
    times = list.count(max_number)
    return f"The highest number in the given list is {max_number} and it shows up {times} times"


# print(highest_number([1, 2, 3, 4, 4, 4, 3, 2, 3, 3, 3]))
# print(highest_number(arr))
# print(highest_number(range(act.inicio, act.fim)))
numbers_list = [0, 1, 3, 5, 7, 9]
megasena = list(range(1, 61))
print(len(list(itertools.combinations(numbers_list, 4))))
print(len(list(itertools.permutations(numbers_list, 6))))
# print(len(list(itertools.combinations(megasena, 6))))
print(random.randint(1, 3))
