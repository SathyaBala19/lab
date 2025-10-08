import math

def tsp(graph, visited, curr_pos, n, count, cost, ans):
    if count == n and graph[curr_pos][0] > 0:
        ans[0] = min(ans[0], cost + graph[curr_pos][0])
        return

    for i in range(n):
        if not visited[i] and graph[curr_pos][i] > 0:
            visited[i] = True
            tsp(graph, visited, i, n, count + 1, cost + graph[curr_pos][i], ans)
            visited[i] = False

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
visited = [False] * n
visited[0] = True
ans = [math.inf]

tsp(graph, visited, 0, n, 1, 0, ans)

print("The minimum cost of the TSP tour is:", ans[0])