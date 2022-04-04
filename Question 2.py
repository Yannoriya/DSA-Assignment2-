
# Link to document:
# https://docs.google.com/document/d/12cIr9gbKcZ0yOydEqD4sTvo8IUDs8IPV6VERTRPV0Ec/edit?usp=sharing

# Number of vertices
vertices_number = 6
# Vertices to form the matrix
vertex = ["v", "w", "z", "u", "x", "y"]

# Define infinity as a large enough value. This value will be used for vertices that are not connected to each other
INF = 99999

# Algorithm implementation
def floyd_warshall(G):
    #This is the output matrix that will finally have the shortest distances between every pair of vertices initializing the solution matrix same as an input  graph matrix
    A = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding all vertices individually to the set of intermediate vertices.

    # Picking all vertices as source one by one
    for k in range(number_vertices):
        # Pick all vertices as destination for the above picked source
        for i in range(number_vertices):
            # If vertex k is on the shortest path from
            # i to j, then update the value of A[i][j]
            for j in range(number_vertices):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    print_solution(A)


# Print solution
def print_solution(A):
    for i in range(number_vertices):
        for j in range(number_vertices):
            if i == 0 and j == 0:
                for index in range(len(vertex)):
                    if index == 0:
                        print("  ", vertex[index], end="  ")
                    elif index == len(vertex) - 1:
                        print(vertex[index]),
                    else:
                        print(vertex[index], end="  ")

            if j == 0:
                print(vertex[i], end="  ")
            if A[i][j] == INF:
                print("INF", end=" ")
            else:
                print(A[i][j], end="  ")

        print(" ")


# Driver code
print("Following matrix shows the shortest distances between every pair of vertices")
G = [[0, 3, INF, 2, 2, INF],
     [3, 0, 5, 5, 3, 1],
     [INF, 5, 0, INF, INF, 1],
     [2, 5, INF, 0, 1, INF],
     [2, 3, INF, 1, 0, 1],
     [INF, 1, 1, INF, 1, 0]]
floyd_warshall(G)
