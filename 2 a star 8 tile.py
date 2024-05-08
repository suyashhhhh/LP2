import heapq

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Function to calculate the number of misplaced tiles heuristic
def calculate_heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Function to get possible next moves
def get_next_moves(state):
    zero_i, zero_j = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_i, zero_j = i, j
                break
    next_moves = []
    movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (up, down, left, right)
    for move in movements:
        move_i, move_j = move
        new_i, new_j = zero_i + move_i, zero_j + move_j
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
            next_moves.append(new_state)
    return next_moves

# Function to perform the A* search algorithm
def a_star_search(start_state):
    open_list = []
    heapq.heappush(open_list, (0, start_state))
    cost_dict = {str(start_state): 0}
    path_dict = {str(start_state): []}

    while open_list:
        current_cost, current_state = heapq.heappop(open_list)

        if current_state == goal_state:
            return path_dict[str(current_state)]

        next_moves = get_next_moves(current_state)

        for move in next_moves:
            new_cost = cost_dict[str(current_state)] + 1
            new_heuristic = calculate_heuristic(move)
            new_total_cost = new_cost + new_heuristic

            if str(move) not in cost_dict or new_cost < cost_dict[str(move)]:
                cost_dict[str(move)] = new_cost
                path_dict[str(move)] = path_dict[str(current_state)] + [move]
                heapq.heappush(open_list, (new_total_cost, move))

    return None

# Perform the A* search with the given start state
# Define the start state
start_state = [[2, 3, 6], [1, 5, 8], [4, 7, 0]]

result = a_star_search(start_state)

if result is None:
    print("Goal state is not reachable from the given start state.")
else:
    print("The optimal path to reach the goal state is:")
    for move in result:
        for row in move:
            print(row)
        print()
