from glob import glob


GRAPH_FILE_EXTENSION = "tsp"


def read_graph(f):
    # lines = f.readlines()
    # n, m = list(map(int, lines[0].split()))

    # g = Graph(n, m)

    # for l in lines[1:]:
    #     l = list(map(int, l.split()))
    #     g.add_edge(l[0], l[1], l[2])

    # return g
    pass


def open_graph(file_path):
    with open(file_path, "r") as f:
        # return read_graph(f)
        return file_path


def read_all(directory_path, size=None):
    files = read_sort_files(directory_path, size)
    return list(map(open_graph, files))


def read_sort_files(directory_path, size=None):
    files = sorted(glob(f"{directory_path}/*.{GRAPH_FILE_EXTENSION}"))
    return files if not size else files[:size]
