def wyszukiwanie_interpolacyjne(lista, szukana):
    start = 0
    end = len(lista)-1
    krok = 0
    while start <= end and lista[start] <= szukana <= lista[end]:
        if lista[start] == lista[end]:
            break
        krok += 1
        mid = int(start + ((szukana - lista[start]) * (end - start)) / (lista[end] - lista[start]))
        print(f"{krok}\t{start}\t{end}\t{mid}\t{lista[mid]}")
        if szukana == lista[mid]:
            return mid
        elif mid < szukana:
            start = mid+1
        else:
            end = mid-1
    return -1


l = [12, 18, 24, 30, 36, 42, 48, 54, 60]
print(wyszukiwanie_interpolacyjne(l, 36))
