import glob
import argparse

from typing import NewType, Tuple

Edge = NewType('Edge', Tuple[Tuple[int, int], int])
Vertex = NewType('Vertex', int)

GRAPH_FILE_EXTENSION = "txt"

class Graph:
  _n = 0
  _m = 0
  
  _adj_list = { }
  _edges = set()

  def __init__ (self, n: int = 0, m: int = 0):
    self._n = n
    self._m = m

    for i in range(1, n + 1):
      self._adj_list.update({i: { }})

  def add_edge(self, e: Edge):
    vs = e[0]
    w = e[1]

    self._adj_list[vs[0]].update({vs[1]: w})
    self._adj_list[vs[1]].update({vs[0]: w})

    self._edges.add(e)

  def get_adj(self, v: Vertex):
    return self._adj_list[v]

  def get_all_edges(self):
    return self._edges

  def create_graph(fd):
    n, m = map(int, next(fd).split())

    graph = Graph(n, m)

    for line in fd:
      a, b, w = list(map(int, line.split()))
      e = Edge(((a, b), w))
      graph.add_edge(e)

    return graph

  def __str__(self):
    return str(self._adj_list)


def init_graph_from_file(file_path):
  with open(file_path) as fd:
    return Graph.create_graph(fd)

def init_graph_from_files(directory_path):
  return list(
    map(
      lambda filename: 
        init_graph_from_file(filename)
      , glob.glob(f'{directory_path}/*.{GRAPH_FILE_EXTENSION}')
    )
  )


def init_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", type=str)
  parser.add_argument("-d", type=str)
  
  return parser


def main():
  args = init_args().parse_args()

  if not args.d and not args.f:
    print("Missing --directory or --file argument")
  elif args.d:
    graphs = init_graph_from_files(args.d)
    for graph in graphs[:3]: print(graph)
  elif args.f:
    graph = init_graph_from_file(args.f)
    print(graph)


if __name__ == "__main__":
  main()