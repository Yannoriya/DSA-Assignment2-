# Importing the needed libraries

import sys

# Initializing a class for the vertices of this graph
class Vertex:
    # Function initializing a vertex
    def _init_(self, key):
        self.id = key
        self.connectedTo = {}

    # Function adding a neighbouring vertex
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # Function returning the identity of the vertex
    def _str_(self):
        return str(self.id)

    # Function connecting two vertices
    def getConnections(self):
        neighbors = {}
        for neighbor in self.connectedTo:
            neighbors[str(neighbor)] = self.connectedTo[neighbor]
        return neighbors

    # Function getting the weight of the vertex
    def getWeight(self, nbr):
        return self.connectedTo[nbr]


# Initializing a class for the graph
class Graph:
  # Function initializing a graph with its vertices and their amount(number of vertices)
    def _init_(self):
        self.vertList = {}
        self.numVertices = 0

    # Function adding a vertex to the graph
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # Function getting the vertex of the graph
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # Function getting the neighbouring vertex of a vertex on the graph
    def getVertexNeighbours(self, n):
        if n in self.vertList:
            return self.vertList[n].getConnections()
        else:
            return None

    # Function returning the vertices contained in the graph
    def _contains_(self, n):
        return n in self.vertList

    # Function adding an edge in a graph
    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        self.vertList[t].addNeighbor(self.vertList[f], weight)

    # Function getting the vertices of the graph
    def getVertices(self):
        return self.vertList.keys()

    # Function getting the iterator of the vertlist of the graph
    def _iter_(self):
        return iter(self.vertList.values())

    # Function printing the solution
    def printSolution(self, dist, x):
        # for node in dist:
        print(" The shortest path of vertex ", x, " from the source is ", dist[x])

    # Function getting the minimum distance
    def minDistance(self, dist, sptSet):

        global min_index
        min = sys.maxsize
        for vertex in self.vertList:
            if dist[vertex] < min and sptSet[vertex] is False:
                min = dist[vertex]
                min_index = vertex

        return min_index

    # Function implementing Dijkstra's algorithm
    def dijkstra(self, src):
        dist = {}
        smallestPathDict = {}
        sourceNeigbors = {}

        if src in self.vertList:
            sourceNeigbors = self.getVertexNeighbours(src)

        for vertex in self.vertList:
            smallestPathDict[vertex] = False
            if vertex in sourceNeigbors:
                dist[vertex] = sourceNeigbors[vertex]
            elif vertex == src:
                dist[src] = 0
            else:
                dist[vertex] = sys.maxsize

        for count in range(self.numVertices):

            x = self.minDistance(dist, smallestPathDict)
            self.printSolution(dist, x)

            smallestPathDict[x] = True
            smallestPathNeighbors = self.getVertexNeighbours(x)

            for vertex in smallestPathNeighbors:
                if smallestPathDict[vertex] is False and dist[vertex] > dist[x] + smallestPathNeighbors[vertex]:
                    dist[vertex] = dist[x] + smallestPathNeighbors[vertex]


# Driver code
g = Graph()
print("The following is information on the shortest path using Dijkstra's algorithm:")
print("The results show the vertices in the order in which they become known and the length of the shortest paths used")
print("NB: The source of the graph is at vertex C")
print()

g.addEdge("A", "B", 13)
g.addEdge("A", "D", 10)
g.addEdge("B", "D", 17)
g.addEdge("B", "E", 20)
g.addEdge("B", "C", 5)
g.addEdge("C", "F", 30)
g.addEdge("B", "F", 18)
g.addEdge("E", "C", 22)

g.dijkstra("C")
