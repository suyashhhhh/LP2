def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # List to store visited vertices
    visited = []

    while len(visited) < len(graph):
        # Find the vertex with the minimum distance
        min_distance = float('inf')
        min_vertex = None

        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        if min_vertex is None:
            # There is no path to the remaining unvisited vertices
            break

        # Add the vertex to the visited list
        visited.append(min_vertex)

        # Update the distances of its neighbors
        for neighbor, weight in graph[min_vertex]:
            distance = distances[min_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances


# Accept graph input from the user
graph = {}

num_edges = int(input("Enter the number of edges: "))

for i in range(num_edges):
    print("\nFor Edge", i+1)

    src = input("Enter start vertex: ")
    dest = input("Enter end vertex: ")
    weight = int(input("Enter weight: "))
          
    # Add the edge to the graph
    if src in graph:
        graph[src].append((dest, weight))
    else:
        graph[src] = [(dest, weight)]

    if dest in graph:
        graph[dest].append((src, weight))
    else:
        graph[dest] = [(src, weight)]


start_vertex = input("Enter the starting vertex: ")

# Apply Dijkstra's algorithm
shortest_distances = dijkstra(graph, start_vertex)

print("\nShortest distances from vertex", start_vertex)
for vertex, distance in shortest_distances.items():
    print("Vertex:", vertex, "Distance:", distance)
