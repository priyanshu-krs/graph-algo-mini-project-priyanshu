import networkx as nx
import matplotlib.pyplot as plt

# Graph definition
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

# Draw graph
plt.figure()
pos = nx.spring_layout(G)  # layout
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos)

plt.title("Graph Visualization (Topological Sort)")
plt.show()