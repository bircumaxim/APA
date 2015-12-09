import sys
INF = sys.maxint
#KRUSKCAL
#######################################################################
def kruskal(graph):
    #connected verticies
    connected = []
    #selected edges
    selected = []
    i = 0
    while (len(connected) != graph.n) and (i < len(graph.data)):
        e = graph.data[i]
        a = contains(connected,e.a) == -1
        b = contains(connected,e.b) == -1
        if (a != b) or len(connected) == 0:
            addIfNotExists(connected,e.a)
            addIfNotExists(connected,e.b)
            selected.append(e)
        i += 1
    return selected
#######################################################################


#KRUSKAL PRIM
#######################################################################
def prim(graph):
    #add 1 as connected !
    connected = [1]
    #selected edges
    selected = []
    edges = graph.data
    while len(connected) != graph.n:
        for e in edges:
            a = contains(connected,e.a)
            b = contains(connected,e.b)
            if ((a == -1 and b != -1)) or (b == -1 and a != -1):
                if a == -1:
                    connected.append(e.a)
                else:
                    connected.append(e.b)
                selected.append(e)
                edges.remove(e)
                break

    return selected
#######################################################################


#FLOYD WARHSALL
#######################################################################
def floydWarshall(matrix, numberOfVertices):
    distances = {0: matrix}
    for k in range(1,numberOfVertices+1):
        distances[k] = {}
        for i in range(1,numberOfVertices+1):
            for j in range(1,numberOfVertices+1):
                distances[k][i,j] = min(distances[k-1][i,j],distances[k-1][i,k] + distances[k-1][k,j])
    return distances[numberOfVertices]
#######################################################################

#FLOYD WARHSALL
#######################################################################
def dijkstra(matrix,n):
    distances = {2: matrix}
    for i in range(2,n+1):
        distances[i] = matrix[1,i]
    candidates = [i+2 for i in range(n-1)]
    while len(candidates) != 0 :
        current = 0
        min = INF
        for i in candidates:
            if min > distances[i]:
                current = i
                min = distances[i]
        for i in range(2,n+1):
            if (distances[i] > distances[current] + matrix[current,i]) :
                distances[i] = distances[current] + matrix[current,i]

        candidates.remove(current)
    return distances[n]
#######################################################################


