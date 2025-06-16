
# A = [11, 3, 2, 105, 5, 6, 8, 10, 2, 3, 7]
A = [5, 4, 17, 3, 2, 1, 10, 9, 8, 7, 6, 5, 1]
# A = [1, 5, 2]

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

# print(buble_sort(A))

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# print(selection_sort(A))

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i
        while arr[j-1] > temp and j > 0:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr

# print(insertion_sort(A))

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    m = n//2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])
    l_n, r_n = len(L), len(R)
    r, l, i = 0, 0, 0
    res = [0]*n

    while l < l_n and r < r_n:
        if L[l] <= R[r]:
            res[i] = L[l]
            l += 1
        else:
            res[i] = R[r]
            r += 1
        i += 1
    while l < l_n:
        res[i] = L[l]
        i += 1
        l += 1
    while r < r_n:
        res[i] = R[r]
        i += 1
        r += 1
    return res

# print(merge_sort(A))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[-1]
    L = [i for i in arr[:-1] if i <= p]
    R = [i for i in arr[:-1] if i > p]

    L = quick_sort(L)
    R = quick_sort(R)
    return L + [p] + R

print(quick_sort(A))
