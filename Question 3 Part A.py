 #Using a Python dictionary to act as an adjacentcy list
graph = {
    'A': ['D', 'B'],
    'D': ['A', 'B'],
    'B': ['A', 'D', 'E', 'F', 'C'],
    'E': ['B', 'C'],
    'C': ['B', 'E', 'F'],
    'F': ['B', 'C']
}

# Creating a set to keep track of visited nodes of the graph.
visited = set()


# Function that will implement the Depth-First algorithm
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
print("The following is the result of the Depth-First Search: ")
dfs(visited, graph, 'C'
