macierz = [
    [5, 3, 4, 2],
    [3, -1, 8, 11],
    [7, 3, 9, 0]
]

for r in macierz:
    print('\t'.join(map(str, r)))


def znajdz_min_max(macierz):
    maksimum = max(map(max, macierz))
    minimum = min(map(min, macierz))

    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            if macierz[i][j] == maksimum:
                macierz[i][j] = 'MAX'
            if macierz[i][j] == minimum:
                macierz[i][j] = 'MIN'
    for wiersz in macierz:
        print('\t'.join(map(str, wiersz)))
    # return macierz


print('')
znajdz_min_max(macierz)
