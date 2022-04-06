from graph_modified import *

class krVertex: 
    def __init__(self, name): 
        self.name = name
        self.parent = None 
        self.visited = 0 
    
    def __repr__(self): 
        #return "Vertex({0})".format(self.name)
        return "Vertex({0})".format(self.name)

    def visit(self):
        self.visited = 1

    def get_name(self): 
        return self.name
    
    def is_visited(self):
        return self.visited 

    def change_parent(self, v): 
        self.parent = v

'''
moved to graph modified
class krEdge: 
    def __init__(self,s , t): 
        self.name = (s, t)
        self.label = None       # None, 0 for discovery, 1 for back 
        self.ancestor = None    # a node which is ancestor, maybe just 1 since need to find cycles

    def get_opposite(self, v): 
        if v == self.name[0]: 
            return self.name[1]
        elif v == self.name[1]: 
            return self.name[0]
        else: 
            return None 
    
    def __repr__(self): 
       #return "Edge({0}, {1})".format(self.name[0], self.name[1])
       return "({0}, {1})".format(self.name[0], self.name[1])
'''

def add_dict(l, acc):
    if len(l) == 0:
        return acc
    else: 
        x = l[0]
        acc[x] = krVertex(x)
        return add_dict(l[1:], acc)

# NEED TO WRITE CYCLE CHECK USING BFS/DFS
# needs list of vertices and list of edges
def cycle_check(graph, v): 
    #V = map(lambda x : {x: krVertex(x)}, graph.get_vertices())
    V = add_dict(graph.get_vertices(), {})
    V[v].visit()
    for e in [graph.get_adj_list_vertex(v)]: 
        if e.get_label() == None: 
            w = e.get_opposite(v); 
            if V[w].is_visited() == 0:
                # EDGES LABELS: None, 0 for discovery, 1 for back 
                e.change_label(0)
                V[w].change_parent(v)
                return cycle_check(graph, w)
            else: 
                e.change_label(1)
                e.add_ancestor(w)
                return True 
    return False 


# BAD ALGORITHM 
def kruscal_algo(graph): 
    E = graph.get_edges()
    E.sort()
    A = []
    V = []  # list of vertices inserted 
    for e in E: 
        v1 = e.get_vert_1()
        v2 = e.get_vert_2()
    return A 

f = open('/Users/dilettarigo/Desktop/advanced-algorithms/assignment-1/dataset-1/input_random_01_10.txt', 'r')
g = read_graph(f)

print(g.adj_list)


V = add_dict(g.get_vertices(), {})
print(V)

#print(cycle_check(g, 1))

print(g.get_adj_list_vertex(1))
