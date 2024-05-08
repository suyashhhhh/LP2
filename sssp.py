def bfs_shortest_path(graph, start):
    queue = [start]  # Queue to store vertices to visit
    distances = {start: 0}  # Dictionary to store the distances from the start vertex

    while queue:
        vertex = queue.pop(0)

        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return distances


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
    graph[dest].append(src)

start_vertex = input("Enter the start vertex: ")

shortest_distances = bfs_shortest_path(graph, start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print(vertex, ":", distance)
