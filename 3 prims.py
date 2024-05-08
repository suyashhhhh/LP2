def prims_algorithm(graph, start_vertex):
    visited = {start_vertex}
    minimum_spanning_tree = []
    edges = []

    while len(visited) < len(graph):
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited:
                    edges.append((weight, vertex, neighbor))

        weight, src, dest = min(edges)
        edges.remove((weight, src, dest))

        if dest not in visited:
            visited.add(dest)
            minimum_spanning_tree.append((src, dest, weight))

    return minimum_spanning_tree


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


start_vertex = input("Enter the starting vertex for finding Minimum Spanning Tree: ")

minimum_spanning_tree = prims_algorithm(graph, start_vertex)

total_cost = 0
for src, dest, weight in minimum_spanning_tree:
    total_cost += weight

print("\nMinimum Spanning Tree:")
for src, dest, weight in minimum_spanning_tree:
    print(src, "-->", dest, ": ", weight)

print("Total Cost:", total_cost)