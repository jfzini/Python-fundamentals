n = 15
sum = 0
counter = 0

while counter <= n:
    sum += counter
    counter += 1
    print(sum)
print(sum)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sum_arr = 0

for c in arr:  # only iterable objects
    sum_arr += c
    print(sum_arr)
print(sum_arr)
