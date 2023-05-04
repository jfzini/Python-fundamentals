# instead of:
new_dict = {}
for num in range(1, 21):
    new_dict[num] = num ** 2

print(new_dict)

# do this:
newer_dict = {num: num ** 2 for num in range(1, 21)}

print(newer_dict)

# with conditional
n_dict = {n: n ** 2 for n in range(1, 21) if n % 2 == 0}

print(n_dict)
