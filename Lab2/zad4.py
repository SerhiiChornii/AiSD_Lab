a = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]


def binary_search(a: list, l: int, r: int,  v: int):
    m = (l + r)//2

    # Jeśli element środkowy równy szyukenej wartości
    # to zwracamy szukaną wartoć oraz ją indeks
    if a[m] == v:
        return (v, m)
    # Jeśli element środkowy mniejszy szyukenej wartości
    # to szukamy wartość w prawej stronie listy
    elif a[m] < v:
        return binary_search(a, m, r, v)
    # Jeśli element środkowy większy szyukenej wartości
    # to szukamy wartość w lewej stronie listy
    elif a[m] > v:
        return binary_search(a, l, m, v)

    # print(f"l: {l}, m: {m}, r: {r} | {a[m]} | {a[l:r+1]}")


print(binary_search(a, 0, len(a)-1, 55))
