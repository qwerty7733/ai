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
