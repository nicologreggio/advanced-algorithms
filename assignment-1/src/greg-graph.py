
import sys
import os
import functools


def do_things(g):
    print(f'\n\n*******\n<DOING STUFF WITH{g}')

def read_file(f):
    h={}
    with open(f) as file:
        nodes, edges = file.readline().strip().split(' ')
        print(f'There are {nodes} nodes and {edges} edges')
        lines = file.readlines()
        for line in lines:
            # print(line)
            e1, e2, w = line.strip().split(' ')
            # print(f'({e1}, {e2}) {w}')
            if e1 not in h:
                h[e1]={}
            if e2 not in h:
                h[e2]={}
            h[e1][e2]=w
            h[e2][e1]=w
        return h


# ========================================
# path='../dataset-1'
path = 0
if not path:
    path = '.'

# os.path.relpath()  -> to get relative path
# os.path.abspath() ...
# os.getcwd() -> print working dir
assert(os.path.exists(path)), "Not a valid path! ("+path+")"
os.chdir(path)

print("you chose: "+os.getcwd())

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
            graph=read_file(os.path.join(root, file))
            do_things(graph)
