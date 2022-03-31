from graph import *

# NEED TO WRITE CYCLE CHECK USING BFS/DFS

# BAD ALGORITHM 
def kruscal_algo(graph): 
    E = graph.get_edges()
    E.sort()
    A = []
    V = []  # list of vertices inserted 
    for e in E: 
        v1 = e.get_vert_1()
        v2 = e.get_vert_2()
        # THIS IS NOT A GOOD CHECK FOR CYCLES
        if not (v1 in V and v2 in V): 
            n = E.pop(0)
            A.append(n)
            V.append(v1)
            V.append(v2)
    return A 