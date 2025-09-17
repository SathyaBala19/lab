import heapq
def dijkstra(V, edges, src):
    graph = {i: [] for i in range(V)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # undirected
    distance = [float('inf')] * V
    distance[src] = 0

    pq = [(0, src)]  # (distance, node)

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distance

V = 5
edges = [
    (0, 1, 2),
    (0, 4, 1),
    (1, 2, 3),
    (4, 2, 2),
    (2, 3, 6)
]
src = 0

result = dijkstra(V, edges, src)
print("Shortest distances from source:", result)
