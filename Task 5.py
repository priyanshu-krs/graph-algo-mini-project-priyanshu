import networkx as nx
import matplotlib.pyplot as plt

# 🔹 Kruskal Functions
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

def kruskal(edges, V):
    edges = sorted(edges, key=lambda x: x[2])
    parent = list(range(V))
    rank = [0]*V

    mst = []

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, w))
            union(parent, rank, u, v)

    return mst


# 🔹 Input Graph
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

V = 4

# Run Kruskal
mst = kruskal(edges, V)
print("Minimum Spanning Tree:", mst)


# 🔹 Create Graph
G = nx.Graph()

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# 🔹 Draw Graph
plt.figure()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Original Graph")
plt.show()


# 🔹 Draw MST separately
G_mst = nx.Graph()

for u, v, w in mst:
    G_mst.add_edge(u, v, weight=w)

plt.figure()
pos = nx.spring_layout(G_mst)

nx.draw(G_mst, pos, with_labels=True)
labels = nx.get_edge_attributes(G_mst, 'weight')
nx.draw_networkx_edge_labels(G_mst, pos, edge_labels=labels)

plt.title("Minimum Spanning Tree (Kruskal)")
plt.show()