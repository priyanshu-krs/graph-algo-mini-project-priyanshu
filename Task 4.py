import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Weighted Graph (same for both)
graph_weighted = {
    0: [(1,4), (2,1)],
    1: [(3,1)],
    2: [(1,2), (3,5)],
    3: []
}

# Convert to edge list for Bellman-Ford
edges = []
for u in graph_weighted:
    for v, w in graph_weighted[u]:
        edges.append((u, v, w))


# 🔹 Dijkstra
def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while pq:
        d, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist


# 🔹 Bellman-Ford
def bellman_ford(edges, V, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V-1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


# Run Algorithms
print("Dijkstra:", dijkstra(graph_weighted, 0))
print("Bellman-Ford:", bellman_ford(edges, 4, 0))


# 🔹 Graph Visualization
G = nx.DiGraph()

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

plt.figure()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Shortest Path Graph (Dijkstra & Bellman-Ford)")
plt.show()