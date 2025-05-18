
graf = {
 'A': {'B', 'C'},
 'B': {'C', 'D'},
 'C': {'D'},
 'D': {}
}

macierz_graf = [[0, 1, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [0, 0, 0, 0]]

lista_kraw = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


print("Macierz sąsiedctwa:", *macierz_graf, sep='\n ')

print("\nLista krawędzi:\n", lista_kraw)
