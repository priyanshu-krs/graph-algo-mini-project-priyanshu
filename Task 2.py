from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# 🔹 Graph
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}

# 🔹 BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    
    return result

print("BFS:", bfs(graph, 0))


# 🔹 DFS
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    result = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

print("DFS:", dfs(graph, 0))


# 🔹 Graph Visualization
G = nx.DiGraph()

for u in graph:
    for v in graph[u]:
        G.add_edge(u, v)

plt.figure()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)
plt.title("BFS & DFS Graph")

plt.show()