import time
import random


def plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi):
    # Tworzymy tablicę dp, gdzie dp[i][j] oznacza maksymalną wartość możliwą
    # do uzyskania przy użyciu pierwszych i przedmiotów i plecaka o pojemności j.
    dp = [[0] * (pojemnosc + 1) for _ in range(liczba_przedmiotow + 1)]

    # Iteracja przez przedmioty
    for i in range(1, liczba_przedmiotow + 1):
        # Iteracja przez możliwe pojemności plecaka
        for j in range(pojemnosc + 1):
            # Jeśli przedmiot i-ty nie mieści się w plecaku o pojemności j,
            # to przepisujemy wartość z wiersza powyżej (nie bierzemy go)
            if wagi[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Możemy albo pominąć przedmiot (dp[i-1][j]),
                # albo dodać go do plecaka i sprawdzić, czy suma wartości jest większa
                dp[i][j] = max(dp[i - 1][j], wartosci[i - 1] + dp[i - 1][j - wagi[i - 1]])

                # Zwracamy największą możliwą wartość dla wszystkich przedmiotów i pełnej pojemności plecaka
    return dp[liczba_przedmiotow][pojemnosc]


def plecak_recursive(i, pojemnosc, wagi, wartosci, memo):
    if i == 0 or pojemnosc == 0:
        return 0

    if (i, pojemnosc) in memo:
        return memo[(i, pojemnosc)]

    # Jeśli przedmiot się nie mieści, pomijamy go
    if wagi[i - 1] > pojemnosc:
        memo[(i, pojemnosc)] = plecak_recursive(i - 1, pojemnosc, wagi, wartosci, memo)
        return memo[(i, pojemnosc)]

    # Dwa przypadki: bierzemy przedmiot albo go pomijamy
    bierzemy = wartosci[i - 1] + plecak_recursive(i - 1, pojemnosc - wagi[i - 1], wagi, wartosci, memo)
    pomijamy = plecak_recursive(i - 1, pojemnosc, wagi, wartosci, memo)

    # Maksymalną wartość zapisujemy do memo
    memo[(i, pojemnosc)] = max(bierzemy, pomijamy)
    return memo[(i, pojemnosc)]


# Testowanie funkcji
liczba_przedmiotow = 4  # Liczba dostępnych przedmiotów
pojemnosc = 7  # Maksymalna pojemność plecaka
wartosci = [1, 4, 5, 7]  # Wartości przedmiotów
wagi = [1, 3, 4, 5]  # Wagi przedmiotów

# Wywołanie funkcji i wyświetlenie wyniku
print("Maksymalna wartość, jaką można uzyskać:", plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi))

wartosci = [1, 4, 5, 7]
wagi = [1, 3, 4, 5]
pojemnosc = 7
liczba_przedmiotow = len(wartosci)

memo = {}
maks_wartosc = plecak_recursive(liczba_przedmiotow, pojemnosc, wagi, wartosci, memo)
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc}")


wartosci = [random.randint(1, 100) for i in range(998)]
wagi = [random.randint(1, 30) for i in range(998)]
pojemnosc = 150
liczba_przedmiotow = len(wartosci)
memo = {}

print(f"Dla n = {liczba_przedmiotow} i C = {pojemnosc}")
start = time.time()
maks_wartosc = plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi)
end = time.time()
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc} | Czas Wykonania: {end-start} | Iteracyjnie")

start = time.time()
maks_wartosc = plecak_recursive(liczba_przedmiotow, pojemnosc, wagi, wartosci, memo)
end = time.time()
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc} | Czas Wykonania: {end-start} | Rekurencyjnie z memoryzacją")


wartosci = [random.randint(1, 100) for i in range(500)]
wagi = [random.randint(1, 30) for i in range(500)]
pojemnosc = 30
liczba_przedmiotow = len(wartosci)
memo = {}

print(f"Dla n = {liczba_przedmiotow} i C = {pojemnosc}")
start = time.time()
maks_wartosc = plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi)
end = time.time()
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc} | Czas Wykonania: {end-start} | Iteracyjnie")

start = time.time()
maks_wartosc = plecak_recursive(liczba_przedmiotow, pojemnosc, wagi, wartosci, memo)
end = time.time()
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc} | Czas Wykonania: {end-start} | Rekurencyjnie z memoryzacją")

wartosci = [random.randint(1, 100) for i in range(80)]
wagi = [random.randint(1, 30) for i in range(80)]
pojemnosc = 10
liczba_przedmiotow = len(wartosci)
memo = {}

print(f"Dla n = {liczba_przedmiotow} i C = {pojemnosc}")
start = time.time()
maks_wartosc = plecak(liczba_przedmiotow, pojemnosc, wartosci, wagi)
end = time.time()
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc} | Czas Wykonania: {end-start} | Iteracyjnie")

start = time.time()
maks_wartosc = plecak_recursive(liczba_przedmiotow, pojemnosc, wagi, wartosci, memo)
end = time.time()
print(f"Maksymalna wartość, jaką możemy uzyskać: {maks_wartosc} | Czas Wykonania: {end-start} | Rekurencyjnie z memoryzacją")

