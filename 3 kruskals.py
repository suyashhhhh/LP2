def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


def kruskals_algorithm(graph):
    minimum_spanning_tree = []
    edges = []

    for src in graph:
        for dest, weight in graph[src]:
            edges.append((weight, src, dest))

    edges.sort()

    parent = {}
    rank = {}

    for vertex in graph:
        parent[vertex] = vertex
        rank[vertex] = 0

    for edge in edges:
        weight, src, dest = edge

        src_root = find(parent, src)
        dest_root = find(parent, dest)

        if src_root != dest_root:
            minimum_spanning_tree.append((src, dest, weight))
            union(parent, rank, src_root, dest_root)

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

minimum_spanning_tree = kruskals_algorithm(graph)

total_cost = 0
for src, dest, weight in minimum_spanning_tree:
    total_cost += weight

print("\nMinimum Spanning Tree:")
for src, dest, weight in minimum_spanning_tree:
    print(src, "-->", dest, ": ", weight)

print("Total Cost:", total_cost)
