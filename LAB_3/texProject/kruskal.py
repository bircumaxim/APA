from algorithms import *
from random import *
from time import *
import matplotlib.pyplot as plt


class edge:
    def __init__(self,a,b,q):
        self.a = a
        self.b = b
        self.q = q

class graph:
    def __init__(self,n,data):
        self.n = n
        self.data = data
        self.data.sort(key=lambda x: x.q)

    def getElement(self,a,b):
        return self.data[a][b]

def generateGraph(n,edges):
    data = []
    connected = []
    unconnected = [i+1 for i in range(n)]
    for i in range(edges):
        #connect all vertex !!! after that random connections
        if(len(unconnected) != 0):
            vertex = unconnected.pop(0)
            randVertex = 0
            if(len(connected) == 0):
                vertex = unconnected.pop(0)
            else:
                randVertex = connected[randint(0,len(connected)-1)]
            addIfNotExists(connected,randVertex)
            addIfNotExists(connected,vertex)
            data.append(edge(vertex,randVertex,randint(1,10)))
        else:
            vertex = randint(1,n)
            randVertex = randint(1,n)
            while randVertex == vertex:
                randVertex = randint(1,n)
            addIfNotExists(connected,randVertex)
            addIfNotExists(connected,vertex)
            data.append(edge(vertex,randVertex,randint(1,10)))
    return graph(n,data)

graphs = []
nums = []
times = {"prim" : [],"kruskal" : []}

#for printing arrray of vertex
def printArr(selected):
    for i in selected:
        print i.a," => ",i.b," = ",i.q

for i in range(4,100):
    graphs.append(generateGraph(i,i*(i-2)))

for g in graphs :
    start = time()
    prim(g)
    end = time()
    times.get("prim").append(end-start)


    start = time()
    kruskal(g)
    end = time()
    times.get("kruskal").append(end-start)

    nums.append(g.n)


plt.plot(nums,times.get("prim"),'r',label="Prim")
plt.plot(nums,times.get("kruskal"),'b',label="Kruskal")
plt.legend()
plt.show()