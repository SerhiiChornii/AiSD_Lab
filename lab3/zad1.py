ciag = input("Wpisz ciąg liczb po przecinkach: ")
ciag = list(map(int, ciag.split(',')))

stos = []

for i in ciag:
    stos.append(i)

while stos:
    print(stos.pop(), end=' ')

