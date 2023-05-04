# instead of:
new_list = []
for num in range(1, 21):
    if num % 2 == 0:
        new_list.append(num)

print(new_list)

# do this:
newer_list = [num for num in range(1, 21) if num % 2 == 0]

print(newer_list)

print(list(map(lambda x: x * 3, newer_list)))
