import heapq

# -----------------------------------------------
# Heuristic: Number of misplaced tiles (h-score)
# -----------------------------------------------
def heuristic(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# -----------------------------------------------
# Get possible moves (neighbors) from current state
# -----------------------------------------------
def get_neighbors(state):
    neighbors = []
    # Find blank tile (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_r, blank_c = i, j

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = blank_r + dr, blank_c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            # Create a copy and swap blank with neighbor
            new_state = [list(row) for row in state]
            new_state[blank_r][blank_c], new_state[nr][nc] = new_state[nr][nc], new_state[blank_r][blank_c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

# -----------------------------------------------
# A* Algorithm
# -----------------------------------------------
def a_star(start, goal):
    start = tuple(tuple(row) for row in start)
    goal  = tuple(tuple(row) for row in goal)

    # Priority queue: (f_score, g_score, state, path)
    open_list = []
    g = 0
    h = heuristic(start, goal)
    f = g + h
    heapq.heappush(open_list, (f, g, start, [start]))

    closed_set = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g  # Return solution path and cost

        if current in closed_set:
            continue
        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in closed_set:
                new_g = g + 1
                new_h = heuristic(neighbor, goal)
                new_f = new_g + new_h
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, -1  # No solution found

# -----------------------------------------------
# Print puzzle state
# -----------------------------------------------
def print_state(state):
    for row in state:
        print(row)
    print()

# -----------------------------------------------
# Main
# -----------------------------------------------
if __name__ == "__main__":
    # Initial State
    start = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]

    # Goal State
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial State:")
    print_state(start)

    print("Goal State:")
    print_state(goal)

    path, cost = a_star(start, goal)

    if path:
        print(f"Solution found in {cost} moves!\n")
        print("Step-by-step solution:")
        for step, state in enumerate(path):
            print(f"Step {step}:")
            print_state(state)
    else:
        print("No solution exists for this puzzle.")
