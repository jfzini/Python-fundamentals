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
