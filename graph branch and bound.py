def is_safe(graph, v, color, colors):
    for i in range(len(graph)):
        if graph[v][i]==1 and colors[i] == color:
            return False
    return True

def calculate_lower_bound(graph, colors, v):
    # Count the number of unique colors used in the already colored vertices
    used_colors = set()
    for i in range(v):
        if colors[i] != -1:
            used_colors.add(colors[i])
    return len(used_colors)


def graph_coloring_branch_and_bound(graph, num_colors):
    num_vertices = len(graph)
    colors = [-1] * num_vertices

    def graph_coloring_util(v):
        if v == num_vertices:
            return True

        # Calculate the lower bound for the remaining vertices
        lower_bound = calculate_lower_bound(graph, colors, v)

        # Try assigning colors to the current vertex 'v'
        for color in range(1, num_colors + 1):
            if is_safe(graph, v, color, colors) and lower_bound < num_colors:
                colors[v] = color

                if graph_coloring_util(v + 1):
                    return True

                colors[v] = -1

        return False

    if graph_coloring_util(0):
        print("Graph can be colored using", num_colors, "colors.")
        print("Coloring:", colors)
    else:
        print("Graph cannot be colored using", num_colors, "colors.")

def graph_coloring_menu():
    print("Graph Coloring Problem\n")

    num_vertices = int(input("Enter the number of vertices in the graph: "))
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    num_edges = int(input("Enter the number of edges in the graph: "))

    for _ in range(num_edges):
        edge = input("Enter an edge (0 1): ").split()
        u, v = int(edge[0]), int(edge[1])
        graph[u][v] = 1
        graph[v][u] = 1

    num_colors = int(input("Enter the number of colors: "))

    graph_coloring_branch_and_bound(graph, num_colors)

graph_coloring_menu()