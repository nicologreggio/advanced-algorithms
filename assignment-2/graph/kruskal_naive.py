from graph.graph import Graph, Vertex, Edge


def DFS_cycle(g: Graph, v: Vertex, parent: Vertex, visited: "list[bool]") -> bool:
    visited[v] = True

    for n in g.get_adj_list_vertex(v):
        if n != parent:
            if visited[n]:
                return True
            else:
                cycle = DFS_cycle(g, n, v, visited)

                if cycle:
                    return True

    return False


def is_acyclic(g: Graph) -> bool:
    vertices = g.get_vertices()
    visited = {v: False for v in vertices}

    for v in vertices:
        if not visited[v]:
            cycle = DFS_cycle(g, v, -1, visited)

            if cycle:
                return False

    return True


def kruskal_naive(g: Graph) -> "list[Edge]":
    edges = sorted(g.get_edges(), key=lambda edge: edge[2])
    mst = []

    tmp = Graph()

    for e in edges:
        u, v, w = e

        tmp.add_edge(u, v, w)

        if is_acyclic(tmp):
            mst.append(e)
        else:
            tmp.remove_edge(u, v)

    return mst
