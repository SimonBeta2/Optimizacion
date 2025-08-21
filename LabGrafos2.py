import matplotlib.pyplot as plt
import networkx as nx
grafo = nx.Graph()
for i in range(1,101):
    grafo.add_node(i)
grafo.add_edge(1,2)
nx.draw(grafo, with_labels=True)
plt.show

    



