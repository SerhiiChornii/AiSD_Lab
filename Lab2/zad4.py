a = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
# print(len(a))

def binary_search(a: list, v: int):
    l = 0
    r = len(a) - 1
    m = len(a)//2
    print(f"l: {l}, m: {m}, r: {r} | {a[m]} | {a}")

    if a[m] == v:
        return (v, m)
    elif a[m] < v:
        return binary_search(a[m:r+1], v)
    elif a[m] > v:
        return binary_search(a[l:m+1], v)

print(binary_search(a, 55))


def binary_search2(a: list, l: int, r: int,  v: int):
    m = (l + r)//2
    print(f"l: {l}, m: {m}, r: {r} | {a[m]} | {a}")

    if a[m] == v:
        return (v, m)
    elif a[m] < v:
        return binary_search2(a, m, r+1, v)
    elif a[m] > v:
        return binary_search2(a, l, m+1, v)

print(binary_search2(a, 0, len(a)-1, 55))
