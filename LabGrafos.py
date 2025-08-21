import networkx as nx
import matplotlib.pyplot as plt
import random
N = 100  # Número de nodos
grafo = nx.Graph()
grafo.add_nodes_from(range(N))

# Definir un diccionario para llevar la cuenta de aristas de cada nodo
aristas_por_nodo = {nodo: random.randint(5, 10) for nodo in grafo.nodes()}  # Número de aristas objetivo por nodo
aristas_actuales = {nodo: 0 for nodo in grafo.nodes()}  # Contador de aristas actuales por nodo

# Agregar aristas aleatorias hasta que cada nodo tenga el número de aristas deseado
while any(aristas_actuales[nodo] < aristas_por_nodo[nodo] for nodo in grafo.nodes()):
    nodo1, nodo2 = random.sample(list(grafo.nodes()), 2)  # Selecciona dos nodos diferentes al azar
    if not grafo.has_edge(nodo1, nodo2):  # Asegurarse de que la arista no exista
        # Asegurarse de no exceder el límite de aristas en ambos nodos
        if aristas_actuales[nodo1] < aristas_por_nodo[nodo1] and aristas_actuales[nodo2] < aristas_por_nodo[nodo2]:
            grafo.add_edge(nodo1, nodo2)
            aristas_actuales[nodo1] += 1
            aristas_actuales[nodo2] += 1

# Imprimir las aristas generadas y el número de aristas por nodo
print("Aristas generadas:", grafo.edges())
print("Aristas actuales por nodo:", aristas_actuales)

# Graficar el grafo
#nx.draw(grafo, with_labels=True, node_color="lightblue", edge_color="gray")
#plt.show()
