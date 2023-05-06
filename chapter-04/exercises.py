# relação dos nomes
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta',
         'Maria', 'Fernando', 'Cláudio']
# estrutura que irá armazenar o número de letras de cada nome
qtd_letras = {}
# calcula o tamanho de cada nome (em número de letras) e armazena o valor
for nome in nomes:
    qtd_letras[nome] = len(nome)

# refactoring using dict comprehension
letter_qnt = {nome: len(nome) for nome in nomes}
# print(qtd_letras)
# print(letter_qnt)
# print(letter_qnt == qtd_letras)


# create a function with default parameters


def circle_area(r, pi=3.14):
    return pi * r ** 2


print(circle_area(8))
