from cv2 import sort
from graph import *
from kruscal import * 
from analysis import *


'''
f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
g = read_graph(f)

def take_second(i):
    return i[1]

v = g.get_vertices()
V = {k: [0, None] for k in v}
e = g.get_edges()
edges = list(e)
sort_edges= sorted(edges, key=take_second)
E = {j[0] : 0 for j in e}
'''

f1 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
f2 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_05_20.txt', 'r')
f3 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_21_200.txt', 'r')
f4 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_32_800.txt', 'r')
f5 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_43_4000.txt', 'r')
f6 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_53_20000.txt', 'r')
f7 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_63_80000.txt', 'r')
f8 = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_68_100000.txt', 'r')

l = [f1, f2, f3, f4]

def readList(l): 
    A = []
    for file in l:
        g = read_graph(file)
        A.append(g)
    return A

#B = readList(l)
path = '/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1'
B = read_all(path)
C = filter(lambda x : x.get_n() < 1000, B)

for g in C: 
    print(len(kruscal(g)))

'''
def b (m, n): 
    return m * n 

run_times, graphs_dimensions, ratios, c_estimates = compute_asymptotic_constant(C, kruscal, b, 100)
'''

# asymptotic_analysis(C, kruscal, 10)
