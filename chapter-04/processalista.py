# Encontra e retorna o maior número impar presente na lista
def maior_impar(lista):
    return max(list(filter(lambda x: x % 2 != 0, lista)))

# Encontra e retorna o menor número impar presente na lista


def menor_impar(lista):
    return min(list(filter(lambda x: x % 2 != 0, lista)))


# Encontra e retorna o maior e o menor número ímpar presentes na lista


def maior_menor_impar(lista):
    return (menor_impar(lista), maior_impar(lista))
