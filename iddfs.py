def depth_limited_dfs(graph, start, goal, depth_limit):
    if start == goal:
        return [start]

    if depth_limit <= 0:
        return None

    if start not in graph:
        return None

    for neighbor in graph[start]:
        path = depth_limited_dfs(graph, neighbor, goal, depth_limit - 1)
        if path is not None:
            return [start] + path

    return None


def iterative_deepening_dfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = depth_limited_dfs(graph, start, goal, depth)
        if path is not None:
            return path

    return None


# Accept graph from the user
graph = {}

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    print("\nFor Edge", i + 1)
    src = input("Enter start vertex: ")
    dest = input("Enter end vertex: ")

    # Add vertices to the graph if they don't exist
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []

    graph[src].append(dest)

start_vertex = input("Enter the start vertex: ")
goal_vertex = input("Enter the goal vertex: ")
max_depth = int(input("Enter the maximum depth: "))

# Find the path from the start to the goal using IDDFS
path = iterative_deepening_dfs(graph, start_vertex, goal_vertex, max_depth)

if path is not None:
    print(f"Path from {start_vertex} to {goal_vertex}: {path}")
else:
    print(f"There is no path from {start_vertex} to {goal_vertex} within the depth limit.")
