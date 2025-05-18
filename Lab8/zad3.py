graf = {
    'A': {'B', 'C', 'D'},
    'B': {'C', 'E'},
    'C': {'A', 'B', 'E'},
    'D': {'A', 'C'},
    'E': {'A', 'C'},
}

def show_wiersz(graf, wiersz):
    for i in graf:
        if i == wiersz:
            print(f"{i}: ", *graf[i])

show_wiersz(graf, 'A')
show_wiersz(graf, 'B')
show_wiersz(graf, 'C')
show_wiersz(graf, 'D')
