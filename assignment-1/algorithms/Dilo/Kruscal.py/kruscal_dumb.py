from graph import *

def take_1(i):
    return i[1]

# non funziona perché se e[0] ed e[1] sono già stati inseriti ma appartengono a componenti connesse diverse non li inserisce... 
def acyclic(E): 
    Q = {}
    for e in E: 
        if e[0] in Q.keys(): 
            if e[1] in Q.keys(): 
                return False
        else: 
            Q.update({e[0] : 0})
        if e[1] not in Q.keys(): 
            Q.update({e[1] : 0})
    return True 

def kruscal(graph): 
    e = graph.get_edges()
    edges = list(e)
    sort_edges = sorted(edges, key=take_1)
    A = {}
    for e in sort_edges: 
        A.update({e[0] : 0})
        if not acyclic(A):
            A.pop(e[0])    
    return A 
