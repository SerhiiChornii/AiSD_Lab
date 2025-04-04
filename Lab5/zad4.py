import heapq

zadania = []
# zadania = heapq.heapify(zadania)

menu = '''\nWybierz działanie:
1. Dodaj zadanie z priorytetem
2. Obsłuż zadanie o najwyższym priorytecie
3. Pokaż kolejkę zadań
4. Zakończ działanie programu\n'''

while True:
    inpt = input("Wpisz działanie: ")
    match inpt.strip().lower():
        case '1':
            zadanie = input("Wpisz zadanie: ")
            if not zadanie:
                print("Nazwa zadanie nie może być pustą")
                continue
            priorytet = int(input("Wpisz priorytet zadania: "))
            heapq.heappush(zadania, (zadanie, priorytet))
        case '2':
            print(heapq.heappop(zadania))
        case '3':
            if zadania:
                for i in zadania:
                    print(i)
        case 'menu' | 'help' | '-h':
            print(menu)
        case 'exit' | '4':
            print("Zakończenie programu")
            break
        case _ :
            print("Wprowadzono niepoprawne działanie")
