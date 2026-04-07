import networkx as nx
import matplotlib.pyplot as plt

# 🔹 Adjacency List
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}

print("Adjacency List:")
print(graph)

# 🔹 Adjacency Matrix
matrix = [
    [0,1,1,0],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,0,0]
]

print("\nAdjacency Matrix:")
for row in matrix:
    print(row)

# 🔹 Graph Visualization
G = nx.DiGraph()

for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor)

plt.figure()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
plt.title("Graph Representation")

plt.show()