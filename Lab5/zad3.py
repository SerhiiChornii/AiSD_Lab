def is_empty(queue: list):
    return not queue

def enqueue(queue: list, el):
    return queue.append(el)

def dequeue(queue: list):
    return queue.pop(0)

def show_queue(queue: list):
    return queue

menu = '''\nWybierz działanie:
1. Zarejestruj pacjenta
2. Wywołaj pacjenta do gabinetu
3. Pokaż aktualną kolejkę
4. Zakończ działanie programu\n'''

print(menu)
kolejka = []
while True:
    inpt = input("Wpisz działanie: ")
    match inpt.strip().lower():
        case '1':
            pacjent = input("Wpisz pacjęta: ")
            if not pacjent:
                print("Imię pacjenta nie może być puste")
                continue
            enqueue(kolejka, pacjent)
        case '2':
            if is_empty(kolejka):
                print("Kolejka jest pusta")
            else:
                print(f"Pacjęt {dequeue(kolejka)} jest wywołany do gabinetu")
        case '3':
            if is_empty(kolejka):
                print("Kolejka jest pusta")
            else:
                print(f"Aktualna kolejka: ", *show_queue(kolejka))
        case 'menu' | 'help' | '-h':
            print(menu)
        case 'exit' | '4':
            print("Zakończenie roboty programu")
            break
        case _ :
            print("Wprowadzono niepoprawne działanie")