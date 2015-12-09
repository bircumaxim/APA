from algorithms import *

import sys
import random
from time import *
import matplotlib.pyplot as plt

INF = sys.maxint

def printGraph(w,n):
    for i in range(1,n+1):
        print
        for j in range(1,n+1):
            if(w[i,j] > 100):
                print "inf",
            else:
                print w[i,j],

def getGraphPattern(n):
    matrix = {}
    for i in range(1,n+1):
        matrix[i,i] = 0
        for j in range(1,n+1):
            matrix.setdefault((i,j), INF)
    return matrix

def generateRandomGraph(n):
    matrix = getGraphPattern(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i != j):
                val = random.randint(1, n)
                if(val == 1):
                    matrix[i,j] = 0
                else:
                    matrix[i,j] = val
    return matrix

def getTime(algorithm,matrix, n):
    start = time()
    algorithm(matrix, n)
    end = time()
    return end - start


vertices = []
timesF = []
timesD = []

for n in range(4,40):
    vertices.append(n)
    w = generateRandomGraph(n)
    timesF.append(getTime(floydWarshall,w,n))
    timesD.append(getTime(dijkstra,w,n))

plt.plot(vertices,timesF,'r',label="Floyd")
plt.plot(vertices,timesD,'b',label="Dijkstra")
plt.legend()
plt.show()