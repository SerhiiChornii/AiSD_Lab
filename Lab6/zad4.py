def insertionSort(A):
    for i in range(1, len(A)):
        wst_el = A[i]
        j = i - 1
        print(f"i: {i}\nwtawiany_el: {wst_el}\nj: {j}")
        print(f"{wst_el} < {A[j]}: {wst_el < A[j]}")
        while j >= 0 and wst_el < A[j]:
            print(f"j2: {j}")
            print(f"{wst_el} < {A[j]}: {wst_el < A[j]}")
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = wst_el
        print(f"Tablica po wstawieniu: {A}")

oceny = [3, 5, 2, 6, 4, 1]
insertionSort(oceny)
print(oceny)
