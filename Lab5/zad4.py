import heapq

zadania = []

menu = '''\nWybierz działanie:
1. Dodaj zadanie z priorytetem
2. Obsłuż zadanie o najwyższym priorytecie
3. Pokaż kolejkę zadań
4. Zakończ działanie programu\n'''

print(menu)
while True:
    inpt = input("Wpisz działanie: ")
    match inpt.strip().lower():
        case '1':
            zadanie = input("Wpisz zadanie: ")
            if not zadanie:
                print("Nazwa zadanie nie może być pustą")
                continue
            priorytet = int(input("Wpisz priorytet zadania: "))
            heapq.heappush(zadania, (priorytet, zadanie))
        case '2':
            if zadania:
                print(heapq.heappop(zadania))
            else:
                print("Kolejka jest pusta")
        case '3':
            if not zadania:
                print("Kolejka jest pusta")
            else:
                for i in zadania:
                    print(i)
        case 'menu' | 'help' | '-h':
            print(menu)
        case 'exit' | '4':
            print("Zakończenie programu")
            break
        case _ :
            print("Wprowadzono niepoprawne działanie")
