<<<<<<< HEAD
ciag = input("Wpisz ciąg liczb po przecinkach: ")
ciag = list(map(int, ciag.split(',')))
=======
ciag = input("Wprowadź ciąg liczb: ")
ciag = list(map(int, ciag.split()))
>>>>>>> aaecbf02883ec423fc517d04fdea8a7484a11d21

stos = []

for i in ciag:
    stos.append(i)

while stos:
    print(stos.pop(), end=' ')
<<<<<<< HEAD

=======
>>>>>>> aaecbf02883ec423fc517d04fdea8a7484a11d21
