def wyszukiwanie_liniowe(lista, szukana_wartosc):
    for i in range(len(lista)):
        if lista[i] == szukana_wartosc:
            return i
    return -1

print(wyszukiwanie_liniowe([1,2,3,4,5,6], 1))
