ciag = input("Wprowadź ciąg liczb: ")
ciag = list(map(int, ciag.split()))

stos = []

for i in ciag:
    stos.append(i)

while stos:
    print(stos.pop(), end=' ')
