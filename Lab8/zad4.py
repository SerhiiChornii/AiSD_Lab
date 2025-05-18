from matplotlib import pyplot as plt
import networkx as nx

lista_sasiedztwa = {
    'A': {'B', 'C'},
    'B': {'A', 'C', 'D', 'E'},
    'C': {'A', 'B', 'E'},
    'D': {'B', 'F'},
    'E': {'B', 'C', 'F'},
    'F': {'D', 'E'},
}

G = nx.Graph()

G.add_nodes_from(lista_sasiedztwa.keys())
for i, edge in enumerate(lista_sasiedztwa.values()):
    print(edge, i)
    node1 = list(lista_sasiedztwa.keys())[i]
    for node2 in edge:
        G.add_edge(node1, node2)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
