from src.graph import Graph

def DFS_cycle(g: Graph, v, parent, visited):
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


def is_acyclic(g: Graph):
  visited = [False] * (g.get_n() + 1)

  for v in g.get_vertices():
    if not visited[v]:
      cycle = DFS_cycle(g, v, -1, visited)

      if cycle: return False

  return True


def kruskal(g: Graph):
  edges = sorted(g.get_edges(), key=lambda edge: edge[1])
  mst = []

  tmp = Graph(g.get_n(), g.get_m())

  for e in edges:
    vertices, w = e
    u, v = vertices

    tmp.add_edge(u, v, w)

    if is_acyclic(tmp):
      mst.append(e)
    else:
      tmp.remove_edge(u, v)

  return mst


def kruskal_behaviour(n, m):
  return n * m
