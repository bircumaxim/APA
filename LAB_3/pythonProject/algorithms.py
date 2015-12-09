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

def addIfNotExists(arr,el):
    for i in arr:
        if i == el:
            return
    arr.append(el)

def contains(arr,el):
    i = 0
    for i in arr:
        if i == el:
            return i
        else:
            i += 1
    return -1

