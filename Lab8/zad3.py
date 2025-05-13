graf = {
    'A': {'B', 'C', 'D'},
    'B': {'C', 'E'},
    'C': {'A', 'B', 'E'},
    'D': {'A', 'C'},
    'E': {'A', 'C'},
}


def show_wiersz(graf):
    for i in graf:
        print(f"{i}: ", *graf[i])


show_wiersz(graf)
