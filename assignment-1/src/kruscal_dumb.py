from graph import * 

def take_1(i):
    return i[1]

def preprocess(graph): 
    v = graph.get_vertices()
    #V = {k: [0, None] for k in v}
    V = {k: 0 for k in v}
    e = graph.get_edges()
    edges = list(e)
    sort_edges= sorted(edges, key=take_1)
    #E = {j[0] : (0, None, j[1]) for j in e}
    E = {j[0] : 0 for j in e}   # 0 for null, 1 for discovery, 2 for back
    return V, E, sort_edges

def incident_edges(E, v): 
    L = []
    for e in E.keys(): 
        if e[0] == v or e[1] == v: 
            L.append(e)
    return L 

def opposite(v, e): 
    if e[0] == v:
        return e[1]
    elif e[1] == v:
        return e[0]
    else: 
        return None 

def acyclic(Q, E, v): 
    Q[v] = 1 
    for e in incident_edges(E, v): 
        if E[e] == 0: 
            w = opposite(v, e)
            if Q[w] == 0: 
                E[e] = 1
                #Q[w][1] = v 
                if not acyclic(Q, E, w): 
                    return False 
            else: 
                return False 
    return True 

def reset(Q): 
    R = dict.fromkeys(Q.keys(), 0)
    return R

def kruscal(graph): 
    Q, E, s_edges = preprocess(graph)
    A = {}
    for e in s_edges:
        A.update({e[0] : E[e[0]]})
        if not(acyclic(Q, A, e[0][0])):
            A.pop(e[0])    
        A = reset(A)
        Q = reset(Q)   
    A = list(A.keys())
    return A 
