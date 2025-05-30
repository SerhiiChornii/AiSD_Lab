from matplotlib import pyplot as plt
import networkx as nx

#A — B
# B — A, C
# C — B, D, F
# D — C, E
# E — D
# F — C


lista_sasiedztwa = {
    'A\n1/13': {'B\n2/12'},
    'B\n2/12': {'A\n1/13', 'C\n3/11'},
    'C\n3/11': {'B\n2/12', 'D\n4/7', 'F\n9/10'},
    'D\n4/7': {'C\n3/11', 'E\n5/6'},
    'E\n5/6': {'D\n4/7'},
    'F\n9/10': {'C\n3/11'},
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
