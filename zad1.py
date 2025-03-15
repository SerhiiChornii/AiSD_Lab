def druga_najwieksza(lista):
    zbior = set(lista)
    zbior.remove(max(zbior))
    return max(zbior)

lista = [1, 2, 3, 4, 5, 6, 6, 3, 5, 2]
print(druga_najwieksza(lista))
