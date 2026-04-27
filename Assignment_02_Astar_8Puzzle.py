# ============================================================
# Assignment No  : 02
# Title          : A* Algorithm for 8-Puzzle Problem
# Problem        : Implement A* informed search for the
#                  8-puzzle game.
#                  f(n) = g(n) + h(n)
#                  g(n) = depth (cost so far)
#                  h(n) = misplaced tiles  OR  Manhattan dist
# Subject        : Lab Practice II (310258) - AI | PCCOER
# CO Mapping     : C318.1
# ============================================================

import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)   # 0 = blank tile

# ─── Heuristics ────────────────────────────────────────────

def h_misplaced(state):
    """Count tiles not in goal position (excludes blank)."""
    return sum(1 for i, v in enumerate(state) if v != 0 and v != GOAL[i])

def h_manhattan(state):
    """Sum of Manhattan distances of each tile from its goal."""
    dist = 0
    for i, v in enumerate(state):
        if v != 0:
            gi = GOAL.index(v)
            dist += abs(i // 3 - gi // 3) + abs(i % 3 - gi % 3)
    return dist

# ─── Neighbour generator ───────────────────────────────────

def neighbours(state):
    s = list(state)
    idx = s.index(0)
    r, c = divmod(idx, 3)
    for dr, dc, mv in [(-1,0,"UP"),(1,0,"DOWN"),(0,-1,"LEFT"),(0,1,"RIGHT")]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr*3 + nc
            ns = s[:]
            ns[idx], ns[ni] = ns[ni], ns[idx]
            yield tuple(ns), mv

# ─── A* Search ─────────────────────────────────────────────

def astar(initial, heuristic):
    """
    A* using OPEN (min-heap) and CLOSED (visited set).
    Returns (moves_list, cost, nodes_explored) or (None,-1,n).
    """
    if initial == GOAL:
        return [], 0, 0

    open_heap = [(heuristic(initial), 0, initial, [])]
    closed = set()
    explored = 0

    while open_heap:
        f, g, state, path = heapq.heappop(open_heap)
        if state in closed:
            continue
        closed.add(state)
        explored += 1
        if state == GOAL:
            return path, g, explored
        for nst, mv in neighbours(state):
            if nst not in closed:
                ng = g + 1
                heapq.heappush(open_heap, (ng + heuristic(nst), ng, nst, path + [mv]))

    return None, -1, explored

# ─── Display helpers ───────────────────────────────────────

def draw(state, label=""):
    if label:
        print(f"  [{label}]")
    for i in range(0, 9, 3):
        print("    " + " | ".join(str(x) if x else "_" for x in state[i:i+3]))
    print()

def replay(initial, moves):
    cur = list(initial)
    draw(tuple(cur), "Initial")
    for i, mv in enumerate(moves, 1):
        idx = cur.index(0)
        r, c = divmod(idx, 3)
        dr = {"UP":-1,"DOWN":1,"LEFT":0,"RIGHT":0}[mv]
        dc = {"UP":0,"DOWN":0,"LEFT":-1,"RIGHT":1}[mv]
        ni = (r+dr)*3+(c+dc)
        cur[idx], cur[ni] = cur[ni], cur[idx]
        draw(tuple(cur), f"Step {i}: {mv}")


if __name__ == "__main__":
    print("=" * 52)
    print("  Assignment 02 — A* Algorithm (8-Puzzle) | PCCOER")
    print("=" * 52)
    print("Enter the initial state row by row (0 = blank tile)")
    print("Example:  2 8 3  /  1 6 4  /  7 0 5")
    print()

    tiles = []
    for i in range(3):
        row = list(map(int, input(f"  Row {i+1}: ").split()))
        if len(row) != 3:
            print("  Error: enter exactly 3 numbers per row.")
            exit(1)
        tiles.extend(row)

    initial = tuple(tiles)

    print()
    draw(initial, "Your Initial State")
    draw(GOAL,    "Goal State")

    print("Select heuristic:")
    print("  1. Misplaced Tiles")
    print("  2. Manhattan Distance")
    h_choice = input("  Choice (1/2): ").strip()

    heuristic = h_misplaced if h_choice != "2" else h_manhattan
    h_name    = "Misplaced Tiles" if h_choice != "2" else "Manhattan Distance"

    print(f"\nRunning A* with [{h_name}] heuristic...")
    path, cost, explored = astar(initial, heuristic)

    if path is None:
        print("  No solution exists for this configuration.")
    else:
        print(f"  ✓ Solved in {cost} move(s) | Nodes explored: {explored}")
        print(f"  Move sequence: {path}")
        show = input("\nShow step-by-step replay? (y/n): ").strip().lower()
        if show == "y":
            replay(initial, path)

    print("─── Complexity Analysis ─────────────────────────────")
    print("  Time  : O(b^d)  b = branching factor (~3), d = depth")
    print("  Space : O(b^d)  — all nodes stored in OPEN + CLOSED")
    print("  f(n)  = g(n) + h(n)")
    print("  g(n)  = depth of node (actual cost from start)")
    print("  h(n)  = heuristic estimate to goal (admissible)")
    print("  Manhattan distance is more informed → fewer nodes explored")
    print("\nConclusion: A* algorithm implemented successfully for 8-puzzle.")
