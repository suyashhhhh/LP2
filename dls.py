def depth_limited_search(graph, start, goal, depth_limit):
    visited = set()

    def dfs(current_node, depth):
        if depth > depth_limit:
            return None

        if current_node == goal:
            return [current_node]

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                path = dfs(neighbor, depth + 1)
                if path is not None:
                    return [current_node] + path

        return None

    return dfs(start, 0)


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
depth_limit = int(input("Enter the depth limit: "))

# Find the path from the start to the goal using depth-limited search
path = depth_limited_search(graph, start_vertex, goal_vertex, depth_limit)

if path is not None:
    print(f"Path from {start_vertex} to {goal_vertex}: {path}")
else:
    print(f"There is no path from {start_vertex} to {goal_vertex} within the depth limit.")
