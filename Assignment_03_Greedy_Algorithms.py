# ============================================================
# Assignment No  : 03  (3A + 3B + 3C + 3D — all in one file)
# Title          : Greedy Search Algorithms
# 3A  Dijkstra's Shortest Path      O(E + V log V)
# 3B  Prim's Minimum Spanning Tree  O(E log V)
# 3C  Kruskal's MST                 O(E log E)
# 3D  Selection Sort                O(n²)
# Subject        : Lab Practice II (310258) - AI | PCCOER
# CO Mapping     : C318.1
# ============================================================
""" sample i/p
Select (1–4): 1

Number of vertices: 5
Number of edges   : 7
Edges as  u v weight:
0 1 2
0 3 6
1 2 3
1 3 1
2 4 5
3 4 4
1 4 9

Source vertex: 0

Select (1–4): 2

Number of vertices: 5
Number of edges   : 7
Edges as  u v weight:
0 1 2
0 3 6
1 2 3
1 3 1
2 4 5
3 4 4
1 4 9

Select (1–4): 3

Number of vertices: 5
Number of edges   : 7
Edges as  u v weight:
0 1 2
0 3 6
1 2 3
1 3 1
2 4 5
3 4 4
1 4 9

Select (1–4): 4

Enter array elements (space-separated): 64 25 12 22 11"""



import heapq

# ═══════════════════════════════════════════════
#  3A — DIJKSTRA'S SHORTEST PATH
# ═══════════════════════════════════════════════

def dijkstra(graph, src, n):
    dist = [float("inf")] * n
    pred = [-1] * n
    seen = [False] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if seen[u]: continue
        seen[u] = True
        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, pred

def get_path(pred, src, tgt):
    path, cur = [], tgt
    while cur != -1:
        path.append(cur)
        if cur == src: break
        cur = pred[cur]
    path.reverse()
    return path if path and path[0] == src else []

def run_dijkstra():
    print("\n" + "═"*48)
    print("  3A — Dijkstra's Shortest Path")
    print("═"*48)
    n = int(input("Number of vertices: "))
    e = int(input("Number of edges   : "))
    graph = {i: [] for i in range(n)}
    print("Edges as  u v weight:")
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w)); graph[v].append((u, w))
    src = int(input("Source vertex: "))
    dist, pred = dijkstra(graph, src, n)
    print(f"\n  {'Vertex':<8}{'Distance':<12}{'Path'}")
    print("  " + "─"*36)
    for v in range(n):
        p = get_path(pred, src, v)
        ps = " → ".join(map(str, p)) if p else "Unreachable"
        print(f"  {v:<8}{str(dist[v]):<12}{ps}")
    print("\n  Complexity: Time Θ(E + V log V) | Space Θ(V)")
    print("  Conclusion: Dijkstra's Shortest Path implemented.")


# ═══════════════════════════════════════════════
#  3B — PRIM'S MST
# ═══════════════════════════════════════════════

def prims(graph, n):
    visited, mst, cost = {0}, [], 0
    heap = [(w, 0, v) for v, w in graph.get(0, [])]
    heapq.heapify(heap)
    while heap and len(visited) < n:
        w, u, v = heapq.heappop(heap)
        if v in visited: continue
        visited.add(v); mst.append((u, v, w)); cost += w
        for nbr, wt in graph.get(v, []):
            if nbr not in visited:
                heapq.heappush(heap, (wt, v, nbr))
    return mst, cost

def run_prims():
    print("\n" + "═"*48)
    print("  3B — Prim's Minimum Spanning Tree")
    print("═"*48)
    n = int(input("Number of vertices: "))
    e = int(input("Number of edges   : "))
    graph = {i: [] for i in range(n)}
    print("Edges as  u v weight:")
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w)); graph[v].append((u, w))
    mst, cost = prims(graph, n)
    print("\n  MST Edges:")
    print(f"  {'Edge':<12}{'Weight'}")
    print("  " + "─"*20)
    for u, v, w in mst:
        print(f"  {u} — {v}        {w}")
    print(f"\n  Total MST Cost = {cost}")
    print("  Complexity: O(E log V) with binary heap")
    print("  Conclusion: Prim's MST implemented.")


# ═══════════════════════════════════════════════
#  3C — KRUSKAL'S MST
# ═══════════════════════════════════════════════

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n)); self.r = [0]*n
    def find(self, x):
        if self.p[x] != x: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False
        if self.r[rx] < self.r[ry]: rx, ry = ry, rx
        self.p[ry] = rx
        if self.r[rx] == self.r[ry]: self.r[rx] += 1
        return True

def kruskal(n, edges):
    edges.sort()
    uf = UnionFind(n); mst, cost = [], 0
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w)); cost += w
            if len(mst) == n-1: break
    return mst, cost

def run_kruskal():
    print("\n" + "═"*48)
    print("  3C — Kruskal's Minimum Spanning Tree")
    print("═"*48)
    n = int(input("Number of vertices: "))
    e = int(input("Number of edges   : "))
    edges = []
    print("Edges as  u v weight:")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    mst, cost = kruskal(n, edges)
    print("\n  MST Edges (sorted by weight processed):")
    print(f"  {'Edge':<12}{'Weight'}")
    print("  " + "─"*20)
    for u, v, w in mst:
        print(f"  {u} — {v}        {w}")
    print(f"\n  Total MST Cost = {cost}")
    print("  Complexity: O(E log E + N log N)")
    print("  Conclusion: Kruskal's MST implemented.")


# ═══════════════════════════════════════════════
#  3D — SELECTION SORT (Greedy)
# ═══════════════════════════════════════════════

def selection_sort(arr):
    a = arr[:]
    steps = []
    for i in range(len(a)-1):
        mi = i
        for j in range(i+1, len(a)):
            if a[j] < a[mi]: mi = j
        if mi != i:
            a[i], a[mi] = a[mi], a[i]
        steps.append((i, mi, a[:]))
    return a, steps

def run_selection_sort():
    print("\n" + "═"*48)
    print("  3D — Selection Sort (Greedy)")
    print("═"*48)
    arr = list(map(int, input("Enter array elements (space-separated): ").split()))
    print(f"\n  Original : {arr}")
    sorted_arr, steps = selection_sort(arr)
    for i, (pos, mpos, state) in enumerate(steps):
        print(f"  Pass {i+1:<3}: min={arr[mpos] if i==0 else state[pos]} placed at index {pos}  → {state}")
    print(f"\n  Sorted   : {sorted_arr}")
    print("  Complexity: Time O(n²) | Space O(1) | Stable: No")
    print("  Conclusion: Selection Sort implemented.")


# ═══════════════════════════════════════════════
#  MAIN MENU
# ═══════════════════════════════════════════════

if __name__ == "__main__":
    print("╔" + "═"*46 + "╗")
    print("║  Assignment 03 — Greedy Algorithms | PCCOER  ║")
    print("╠" + "═"*46 + "╣")
    print("║  1. Dijkstra's Shortest Path          (3A)   ║")
    print("║  2. Prim's Minimum Spanning Tree      (3B)   ║")
    print("║  3. Kruskal's Minimum Spanning Tree   (3C)   ║")
    print("║  4. Selection Sort                    (3D)   ║")
    print("╚" + "═"*46 + "╝")

    c = input("\nSelect (1–4): ").strip()
    if   c == "1": run_dijkstra()
    elif c == "2": run_prims()
    elif c == "3": run_kruskal()
    elif c == "4": run_selection_sort()
    else: print("  Invalid choice.")
