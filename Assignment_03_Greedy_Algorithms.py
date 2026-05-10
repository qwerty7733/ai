# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        mi = min(range(i, len(arr)), key=lambda x: arr[x])
        arr[i], arr[mi] = arr[mi], arr[i]
    return arr

# Dijkstra
import heapq
def dijkstra(graph, src, n):
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    print(dist)

# Prim's MST
def prims(graph, n):
    visited, cost = {0}, 0
    heap = [(w, v) for v, w in graph[0]]
    heapq.heapify(heap)
    while heap:
        w, v = heapq.heappop(heap)
        if v in visited: continue
        visited.add(v); cost += w
        for nbr, wt in graph[v]:
            if nbr not in visited:
                heapq.heappush(heap, (wt, nbr))
    print("MST cost:", cost)

# Kruskal's MST
def kruskal(n, edges):
    parent = list(range(n))
    def find(x): 
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        parent[find(x)] = find(y)
    edges.sort()
    cost = 0
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v); cost += w
    print("MST cost:", cost)


if __name__ == "__main__":
    print(selection_sort([64, 25, 12, 22, 11]))

    graph = {0: [(1,2),(3,6)], 1: [(0,2),(2,3),(3,1),(4,9)],
             2: [(1,3),(4,5)], 3: [(0,6),(1,1),(4,4)], 4: [(2,5),(3,4),(1,9)]}
    dijkstra(graph, 0, 5)
    prims(graph, 5)

    edges = [(2,0,1),(6,0,3),(3,1,2),(1,1,3),(5,2,4),(4,3,4),(9,1,4)]
    kruskal(5, edges)
