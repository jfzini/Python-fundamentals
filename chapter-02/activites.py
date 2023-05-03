# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)

# verifica quais números são divisíveis por cinco, dois e sete,
# e exibe aqueles que são
for numero in range(100, 501):
    if numero % 5 == 0 and numero % 2 == 0 and numero % 7 == 0:
        print(numero)

# Altere o código da atividade 1, criando uma variável divisor e, em seguida,
# verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e
# excluindo o 1000) são múltiplos da variável divisor.
# Exemplo, se o valor de divisor for igual a 3, todos os números múltiplos
# de 3, dentro do intervalo, deverão ser exibidos (0, 3, 6, 9, ..., 996, 999).

divisor = 3

for numero in range(0, 1000):
    if numero % 3 == 0:
        print(numero)

# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

# Transforme todos os caracteres das variáveis em maiúsculo;
string_list = [nome, cidade, cpf]
upper_case_list = []

for string in string_list:
    upper_case_list.append(string.upper())

print(upper_case_list)

# Transforme todos os caracteres das variáveis em minúsculo;
lower_case_list = []

for string in string_list:
    lower_case_list.append(string.lower())

print(lower_case_list)

# Exiba a posição do caractere ã, se presente, em cada uma das variáveis;

for string in string_list:
    print(string.find('ã'))

# Exiba o número de caracteres de cada variável;

for string in string_list:
    print(len(string))

# Remova os pontos (.) e o hífen (–) da variável cpf.
replacements = {'-': '', '.': ''}
for old, new in replacements.items():
    cpf = cpf.replace(old, new)
print(cpf)
