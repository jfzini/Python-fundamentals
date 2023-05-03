set1 = {'Ana', 'Beatriz', 'José', 'Carlos', 'Amanda', 'Juliana'}
set2 = {'Ana Flávia', 'Beatriz', 'José Alfredo', 'Carlos André',
        'Amanda', 'Juliana'}
set3 = {'Ana Rita', 'Beatriz', 'José Machado', 'Carlos', 'Amanda',
        'Juliana Souza'}

union_set = set1 | set2 | set3
union_sorted = sorted(union_set)  # set doesnt really sort strings
# so the output is a list
print(union_sorted)
