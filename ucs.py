import heapq

def uniform_cost_search(graph, start, goal):
    # Create a priority queue to store vertices to visit
    queue = [(0, start, [start])]  # (cost, vertex, path)
    visited = set()  # Set to store visited vertices

    while queue:
        cost, vertex, path = heapq.heappop(queue)

        if vertex == goal:
            # Goal vertex reached, return the path and cost
            return path, cost

        if vertex not in visited:
            visited.add(vertex)

            # Expand the current vertex by considering its neighbors
            for neighbor, edge_cost in graph[vertex]:
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_cost, neighbor, new_path))

    # Goal vertex not reachable from the start vertex
    return None


# Accept graph from the user
graph = {}

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    print("\nFor Edge", i + 1)
    src = input("Enter start vertex: ")
    dest = input("Enter end vertex: ")
    cost = float(input("Enter edge cost: "))

    # Add vertices to the graph if they don't exist
    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []

    graph[src].append((dest, cost))
    graph[dest].append((src, cost))

start_vertex = input("Enter the start vertex: ")
goal_vertex = input("Enter the goal vertex: ")

# Find the shortest path and its cost from the start to the goal
shortest_path, shortest_cost = uniform_cost_search(graph, start_vertex, goal_vertex)

if shortest_path is not None:
    print(f"The shortest path from {start_vertex} to {goal_vertex} is: {shortest_path}")
    print(f"The shortest path cost is: {shortest_cost}")
else:
    print(f"There is no path from {start_vertex} to {goal_vertex}")
