def wyszukiwanie_interpolacyjne(lista, szukana):
    start = 0
    end = len(lista)-1

    while start <= end and lista[start] <= szukana <= lista[end]:
        if lista[start] == lista[end]:
            break
        
        mid = int(start + ((szukana - lista[start]) * (end - start)) / (lista[end] - lista[start]))

        if szukana == lista[mid]:
            return mid
        elif mid < szukana:
            start = mid+1
        else:
            end = mid-1
    return -1


l = [1, 2, 3, 4, 5, 6]
start = 0
end = len(l) - 1
print(wyszukiwanie_interpolacyjne(l, 1))
