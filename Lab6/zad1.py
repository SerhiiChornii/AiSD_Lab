
players_n = int(input("Wpisz liczbę graczy: "))
scores = []

for i in range(1, players_n+1):
    score = int(input(f"Wpisz wynik gracza {i}: "))
    scores.append(score)


def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[j] > l[i]:
                l[j], l[i] = l[i], l[j]
    return l

print(f"Wyniki graczy: {scores}")
scores_s = bubble_sort(scores)
print(f"Posortowane wyniki graczy: {scores_s}")
print(f"Największy wynik: {scores_s[-1]}")
print(f"Najmniejszy wynik: {scores_s[0]}")

