from graph import * 
from kruscal_algo import *
from prim_algo import *

f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
g = readGraph(f)

print(g.adlist)
E = g.get_edges()
print("Edges:")
print(E)
print("Prim algo result:")
print(prim_algo(g, 1))
print("Kruscal algo result:")
print(kruscal_algo(g))