import heapq

goal = ((1,2,3),(4,5,6),(7,8,0))

def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i+dr, j+dc
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        s = [list(r) for r in state]
                        s[i][j], s[ni][nj] = s[ni][nj], s[i][j]
                        neighbors.append(tuple(tuple(r) for r in s))
    return neighbors

def a_star(start):
    start = tuple(tuple(r) for r in start)
    pq = [(heuristic(start), 0, start)]
    visited = set()
    while pq:
        f, g, cur = heapq.heappop(pq)
        if cur == goal:
            print("Solved in", g, "moves!")
            return
        if cur in visited:
            continue
        visited.add(cur)
        for nb in get_neighbors(cur):
            if nb not in visited:
                heapq.heappush(pq, (g+1+heuristic(nb), g+1, nb))
    print("No solution found")

start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

a_star(start)



"""A* Algorithm for 8-Puzzle:
1. Define goal state = [[1,2,3],[4,5,6],[7,8,0]]

2. Heuristic h(n):
   - Count misplaced tiles (excluding blank)

3. Start:
   - Add start state to open list
   - f = g + h  (g = moves so far, h = misplaced tiles)

4. Loop:
   - Pick state with lowest f from open list
   - If current == goal → print moves, stop
   - Mark current as visited
   - Find blank tile (0) position
   - Move blank Up, Down, Left, Right (if valid)
   - For each neighbor:
       - If not visited:
           - new_g = g + 1
           - new_f = new_g + h(neighbor)
           - Add to open list

5. If open list empty → No solution

Key terms for viva:

g(n) = cost from start to current state (number of moves)
h(n) = heuristic (misplaced tiles)
f(n) = g(n) + h(n) → total estimated cost
Admissible → misplaced tiles never overestimates, so A* gives optimal solution"""
