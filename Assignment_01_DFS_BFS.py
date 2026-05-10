graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1, 5],
    4: [1, 2, 5],
    5: [3, 4]
}

visited = set()
def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for nbr in graph[node]:
            dfs(nbr)

from collections import deque
def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        print(node, end=" ")
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)

print("DFS:"); dfs(0)
print("\nBFS:"); bfs(0)
