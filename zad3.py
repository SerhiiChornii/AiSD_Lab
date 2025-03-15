def wynik(i):
    if i < 5:
        return 2 # Zmieniona wartość bazowa
    elif i % 2 == 0: # Jeśli i jest parzyste
        return wynik(i - 4) + wynik(i - 2) + 2
    else: # Jeśli i jest nieparzyste
        return wynik(i - 2) % 9 # Zmieniona operacja mod

for i in range(1, 16):
    print(f"i = {i} => {wynik(i)}")