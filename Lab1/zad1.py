import time


def druga_najwieksza(lista):
    zbior = set(lista)
    zbior.remove(max(zbior))
    return max(zbior)


def druga_najwieksza2(lista):
    zbior = list(set(lista))
    zbior = sorted(zbior)
    return zbior[-2]


def druga_najwieksza3(lista):
    maks = float('-inf')
    maks2 = float('-inf')

    for i in lista:
        if i > maks:
            maks2 = maks
            maks = i
        elif maks > i > maks2:
            maks2 = i
    return maks2


lista = [i for i in range(10_000_000)]
# lista = [1, 2, 3, 4, 5] * 2_000_000


time_start1 = time.time()
n1 = druga_najwieksza(lista)
time_end1 = time.time()
time_d1 = time_end1 - time_start1
print(f"n = {n1}, and it takes {time_d1} ms to run")

time_start2 = time.time()
n2 = druga_najwieksza2(lista)
time_end2 = time.time()
time_d2 = time_end2 - time_start2
print(f"n = {n2}, and it takes {time_d2} ms to run")

time_start3 = time.time()
n3 = druga_najwieksza3(lista)
time_end3 = time.time()
time_d3 = time_end3 - time_start3
print(f"n = {n3}, and it takes {time_d3} ms to run")
