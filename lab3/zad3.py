history = []

while True:
    text = input("Dodaj tekst:\n>  ")
    print(history)
    match text.strip().lower():
        case 'undo':
            if not history:
                print("Cofanie nie jest już możliwe!!!")
                continue
            print(history.pop())
        case 'exit':
            break
        case _:
            history.append(text)
