def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # Push unvisited neighbors onto the stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)


def bfs_iterative(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            # Enqueue unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Accepting the graph from the user
graph = {}
vertices = int(input("Enter the number of vertices: "))

for i in range(vertices):
    vertex = input("Enter a vertex: ")
    adjacent_vertices = input("Enter adjacent vertices (space-separated): ").split()
    graph[vertex] = adjacent_vertices

start_vertex = input("Enter the start vertex: ")

# Performing iterative DFS traversal
print("DFS Traversal:")
dfs_iterative(graph, start_vertex)
print()

# Performing iterative BFS traversal
print("BFS Traversal:")
bfs_iterative(graph, start_vertex)
print()
