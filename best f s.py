from queue import PriorityQueue


def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    path = []

    while not priority_queue.empty():
        _, current_node = priority_queue.get()

        if current_node == goal:
            path.append(current_node)
            break

        if current_node not in visited:
            path.append(current_node)
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    priority_queue.put((graph[current_node][neighbor], neighbor))

    if path[-1] != goal:
        return None

    return path


# Accept graph from the user
graph = {}

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    print("\nFor Edge", i + 1)
    src = input("Enter start vertex: ")
    dest = input("Enter end vertex: ")
    weight = int(input("Enter weight: "))

    # Add vertices to the graph if they don't exist
    if src not in graph:
        graph[src] = {}
    if dest not in graph:
        graph[dest] = {}

    graph[src][dest] = weight

start_vertex = input("Enter the start vertex: ")
goal_vertex = input("Enter the goal vertex: ")

# Find the path from the start to the goal using Best-First Search
path = best_first_search(graph, start_vertex, goal_vertex)

if path is not None:
    print(f"Path from {start_vertex} to {goal_vertex}: {path}")
else:
    print(f"There is no path from {start_vertex} to {goal_vertex} using Best-First Search.")
