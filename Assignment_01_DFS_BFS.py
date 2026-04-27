# ============================================================
# Assignment No  : 01
# Title          : DFS and BFS using Recursive Algorithm
# Problem        : Implement Depth First Search and Breadth
#                  First Search on an undirected graph using
#                  recursive functions.
# Subject        : Lab Practice II (310258) - AI | PCCOER
# CO Mapping     : C318.1
# Time Complexity: O(V + E)  |  Space Complexity: O(V)
# ============================================================

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # ─── DFS (Recursive) ───────────────────────────────────

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=" ")
        for nbr in sorted(self.graph[node]):
            if nbr not in visited:
                self.dfs(nbr, visited)
        return visited

    def dfs_search(self, src, key, visited=None):
        if visited is None:
            visited = set()
        if src == key:
            return True
        visited.add(src)
        for nbr in self.graph[src]:
            if nbr not in visited:
                if self.dfs_search(nbr, key, visited):
                    return True
        return False

    # ─── BFS (Recursive) ───────────────────────────────────

    def _bfs_helper(self, q, visited):
        if not q:
            return
        node = q.popleft()
        print(node, end=" ")
        for nbr in sorted(self.graph[node]):
            if nbr not in visited:
                visited.add(nbr)
                q.append(nbr)
        self._bfs_helper(q, visited)

    def bfs(self, start):
        visited = {start}
        self._bfs_helper(deque([start]), visited)

    def bfs_search(self, q, visited, key):
        if not q:
            return "Not Found"
        v = q.popleft()
        if v == key:
            return "Found"
        for u in self.graph[v]:
            if u not in visited:
                visited.add(u)
                q.append(u)
        return self.bfs_search(q, visited, key)


if __name__ == "__main__":
    print("=" * 50)
    print("  Assignment 01 — DFS & BFS (Recursive) | PCCOER")
    print("=" * 50)

    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges   : "))

    g = Graph()
    print("Enter each edge as  u v  (0-indexed, space-separated):")
    for _ in range(e):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    print("\nAdjacency List:")
    for node in sorted(g.graph):
        print(f"  {node} → {sorted(g.graph[node])}")

    start = int(input("\nStart node for traversal: "))

    print(f"\nDFS Traversal from node {start}:")
    print("  ", end="")
    g.dfs(start)

    print(f"\n\nBFS Traversal from node {start}:")
    print("  ", end="")
    g.bfs(start)
    print()

    key = int(input("\nNode to search for: "))

    dfs_result = g.dfs_search(start, key)
    print(f"DFS Search for node {key}: {'Found' if dfs_result else 'Not Found'}")

    q = deque([start])
    vis = {start}
    bfs_result = g.bfs_search(q, vis, key)
    print(f"BFS Search for node {key}: {bfs_result}")

    print("\n─── Complexity Analysis ───────────────────────────")
    print("  DFS → Time: O(V+E) | Space: O(V) | Uses Stack")
    print("  BFS → Time: O(V+E) | Space: O(V) | Uses Queue")
    print("  BFS can find shortest path; DFS cannot guarantee it.")
    print("\nConclusion: Implemented recursive DFS and BFS successfully.")
