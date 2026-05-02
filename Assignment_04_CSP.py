# ============================================================
# Assignment No  : 04
# Title          : Constraint Satisfaction Problem (CSP)
#                  Branch-and-Bound + Backtracking
# Solves         : (A) Graph Coloring  (B) N-Queens
# Subject        : Lab Practice II (310258) - AI | PCCOER
# CO Mapping     : C318.2
# ============================================================

# ═══════════════════════════════════════════════
#  PART A — GRAPH COLORING
# ═══════════════════════════════════════════════
"""sample i/p
Select (1/2): 1

Number of vertices: 5
Number of edges   : 6
Enter each edge as  u v  (0-indexed):
0 1
0 2
1 2
1 3
2 4
3 4"""

def safe_color(graph, color, v, c, n):
    for u in range(n):
        if graph[v][u] == 1 and color[u] == c:
            return False
    return True

def color_bt(graph, m, v, color, n):
    if v == n:
        return True
    for c in range(1, m+1):
        if safe_color(graph, color, v, c, n):
            color[v] = c
            if color_bt(graph, m, v+1, color, n):
                return True
            color[v] = 0
    return False

def solve_coloring(graph, n):
    for m in range(1, n+1):
        color = [0]*n
        if color_bt(graph, m, 0, color, n):
            return m, color
    return -1, []

def verify_coloring(graph, color, n):
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == 1 and color[i] == color[j]:
                return False
    return True

CNAMES = {1:"Red",2:"Green",3:"Blue",4:"Yellow",5:"Purple",6:"Orange"}

def run_graph_coloring():
    print("\n" + "═"*50)
    print("  Graph Coloring — CSP Backtracking")
    print("═"*50)
    n = int(input("Number of vertices: "))
    e = int(input("Number of edges   : "))
    graph = [[0]*n for _ in range(n)]
    print("Enter each edge as  u v  (0-indexed):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u][v] = graph[v][u] = 1

    print("\n  Adjacency Matrix:")
    header = "  " + "".join(f"  {i}" for i in range(n))
    print(header)
    for i in range(n):
        print(f"  {i}" + "".join(f"  {graph[i][j]}" for j in range(n)))

    m, color = solve_coloring(graph, n)
    if m == -1:
        print("\n  No valid coloring found.")
    else:
        print(f"\n  Chromatic Number = {m}  (minimum colors needed)")
        print(f"  {'Vertex':<10}{'Color#':<10}{'Color'}")
        print("  " + "─"*30)
        for i, c in enumerate(color):
            print(f"  {i:<10}{c:<10}{CNAMES.get(c, f'Color{c}')}")
        ok = verify_coloring(graph, color, n)
        print(f"\n  Validation: {'✓ Valid coloring!' if ok else '✗ Invalid!'}")
    print("\n  Complexity: O(m^V) worst case, pruned by backtracking")
    print("  Conclusion: Graph Coloring CSP solved successfully.")


# ═══════════════════════════════════════════════
#  PART B — N-QUEENS
# ═══════════════════════════════════════════════

def safe_queen(board, row, col):
    for r in range(row):
        if board[r] == col: return False
        if abs(board[r] - col) == abs(r - row): return False
    return True

def solve_queens(board, row, n, sols):
    if row == n:
        sols.append(board[:]); return
    for col in range(n):
        if safe_queen(board, row, col):
            board[row] = col
            solve_queens(board, row+1, n, sols)
            board[row] = -1

def draw_board(sol, n):
    border = "  +" + "───+"*n
    print(border)
    for row in range(n):
        line = "  |" + "".join(" Q |" if sol[row]==col else "   |" for col in range(n))
        print(line); print(border)

def run_nqueens():
    print("\n" + "═"*50)
    print("  N-Queens — Backtracking CSP")
    print("═"*50)
    n = int(input("Enter N (board size, e.g. 4 or 8): "))
    board = [-1]*n; sols = []
    solve_queens(board, 0, n, sols)

    if not sols:
        print(f"  No solution for {n}-Queens.")
    else:
        print(f"\n  Total solutions for {n}-Queens: {len(sols)}")
        try:
            show = int(input(f"  Display how many? (1–{min(len(sols),5)}): "))
        except ValueError:
            show = 1
        for i in range(min(show, len(sols))):
            print(f"\n  Solution {i+1}: {sols[i]}")
            draw_board(sols[i], n)

    print("\n  Complexity: O(N!) worst case, heavily pruned")
    print("  Conclusion: N-Queens solved via backtracking.")


# ═══════════════════════════════════════════════
#  MAIN MENU
# ═══════════════════════════════════════════════

if __name__ == "__main__":
    print("╔" + "═"*46 + "╗")
    print("║  Assignment 04 — CSP (Backtracking) | PCCOER ║")
    print("╠" + "═"*46 + "╣")
    print("║  1. Graph Coloring (Branch & Bound)           ║")
    print("║  2. N-Queens Problem                          ║")
    print("╚" + "═"*46 + "╝")

    c = input("\nSelect (1/2): ").strip()
    if   c == "1": run_graph_coloring()
    elif c == "2": run_nqueens()
    else: print("  Invalid choice.")
