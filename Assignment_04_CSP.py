# ---- N-Queens ----
def is_safe(board, row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(board, row, n, sols):
    if row == n:
        sols.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n, sols)
            board[row] = -1

n = 4
sols = []
solve([-1] * n, 0, n, sols)
print("Total solutions:", len(sols))
for s in sols[:2]:
    print(s)


# ---- Graph Coloring ----
def is_safe_color(graph, color, v, c):
    for u in range(len(graph)):
        if graph[v][u] == 1 and color[u] == c:
            return False
    return True

def color_bt(graph, m, v, color):
    n = len(graph)
    if v == n:
        return True
    for c in range(1, m + 1):
        if is_safe_color(graph, color, v, c):
            color[v] = c
            if color_bt(graph, m, v + 1, color):
                return True
            color[v] = 0
    return False

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]
n = len(graph)
for m in range(1, n + 1):
    color = [0] * n
    if color_bt(graph, m, 0, color):
        print("Min colors:", m)
        print("Coloring:", color)
        break



"""N-Queens Algorithm:
1. Start with empty board, place queen row by row
2. For each row, try every column
3. Check if placing queen is safe:
   - No queen in same column
   - No queen on same diagonal
4. If safe, place queen and move to next row
5. If not safe, try next column (backtrack)
6. If all rows filled, store solution

Graph Coloring Algorithm:
1. Start with vertex 0, try to assign colors one by one
2. For each vertex, try colors 1, 2, 3... m
3. Check if color is safe:
   - No adjacent vertex has same color
4. If safe, assign color and move to next vertex
5. If no color works, backtrack to previous vertex
6. Try increasing m (number of colors) until solution found
7. Minimum m used = chromatic number"""
