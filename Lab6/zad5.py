wagi_paczek = [18, 5, 12, 3, 9]

def selection_sort(lista):
    n = len(lista)
    porownania = 0

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            porownania += 1
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        print(f"{i+1} iteracja: {lista}")

    print(f"\nŁączna liczba porównań: {porownania}")

print(f"Paczki: {wagi_paczek}")
selection_sort(wagi_paczek)
print(f"Paczki posortowane: {wagi_paczek}")

