def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()

    if not queue:
        return

    next_queue = []
    for vertex in queue:
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            next_queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

    bfs_recursive(graph, next_queue, visited)


# Accepting the graph from the user
graph = {}
vertices = int(input("Enter the number of vertices: "))

for i in range(vertices):
    vertex = input("Enter a vertex: ")
    adjacent_vertices = input("Enter adjacent vertices (space-separated): ").split()
    graph[vertex] = adjacent_vertices

start_vertex = input("Enter the start vertex: ")

# Performing DFS traversal
print("DFS Traversal:")
dfs_recursive(graph, start_vertex)
print()

# Performing BFS traversal
print("BFS Traversal:")
bfs_recursive(graph, [start_vertex])
print()
