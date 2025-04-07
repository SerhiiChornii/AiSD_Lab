def add_client(queue: list[tuple | None], name: str, time: int):
    return queue.append((name, time))

def serve_client(queue: list[tuple | None]):
    if not queue:
        return (None, None)
    return queue.pop(0)

def show_queue(queue: list[tuple | None]):
    if not queue:
        return "Kolejka jest pusta"
    time = 0
    res = 'Kolejka:'
    for c, t in queue:
        time += t
        res += f"\nKlient {c} zostane obsłużony za {time} minut"
    return res

menu = '''\nWybierz działanie:
1. Dodaj klienta do kolejki
2. Obsłuż klienta
3. Pokaż kolejkę
4. Zakończ działanie programu\n'''

kolejka = []

print(menu)
while True:
    inpt = input("Wpisz działanie: ")
    match inpt.strip().lower():
        case '1':
            c_name = input("Wpisz imię klienta: ")
            if not c_name: 
                print("Imie nie może być puste") 
                continue
            c_time = int(input("Wpisz czas obsługi klienta(w minutach): "))

            add_client(kolejka, c_name, c_time)
        case '2':
            client, time = serve_client(kolejka)
            if not client and not time:
                print("Kolejka jest pusta")
            else:
                print(f"Klient {client} został obsłużony za {time} minut")
        case '3':
            print(show_queue(kolejka))
        case 'menu' | 'help' | '-h':
            print(menu)
        case 'exit' | '4':
            print("Zakończenie programu")
            break
        case _ :
            print("Wprowadzono niepoprawne działanie")
