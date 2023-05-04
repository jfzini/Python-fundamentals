from control import arr


def sum(a, b):
    return a + b


print(sum(4, 5))


def highest_number(list):
    max_number = max(list)
    times = list.count(max_number)
    return f"The highest number in the given list is {max_number} and it shows up {times} times"


print(highest_number([1, 2, 3, 4, 4, 4, 3, 2, 3, 3, 3]))
print(highest_number(arr))
