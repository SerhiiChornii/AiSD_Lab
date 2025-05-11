def wyszukiwanie_liniowe(lista, szukana_wartosc):
    for i in range(len(lista)):
        if lista[i] == szukana_wartosc:
            return i
    return -1


l = [1,2,3,4,5,6]

print(f"lista: {l}\n {1} jest w miejscu: {wyszukiwanie_liniowe(l, 1)}")
print(f"lista: {l}\n {7} jest w miejscu: {wyszukiwanie_liniowe(l, 7)}")
