# Advanced Algorithms
[Advanced Algorithms assignments](https://github.com/nicologreggio/advanced-algorithms/) ; Master's Degree in Computer Science @ UniPd

## Table of contents
- [Assignment 1](#assignment-1---minimum-spanning-tree)
    - [Algorithms](#algorithms)
    - [Dataset](#dataset)
    - [Questions](#question-1)
    - [What to deliver](#what-to-deliver)
    - [Final remarks](#final-remarks)
- [Assignment 2](#assignment-2---traveling-salesman-problem)
    - [Algorithms](#algorithms-1)
    - [Dataset](#dataset-1)
    - [Questions](#question-1-1)
    - [What to deliver](#what-to-deliver-1)
    - [Final remarks](#final-remarks-1)
### Useful links
- [Board 1](https://github.com/nicologreggio/advanced-algorithms/projects/1)
- [Board 2](https://github.com/nicologreggio/advanced-algorithms/projects/2)
- [Milestones](https://github.com/nicologreggio/advanced-algorithms/milestones)

## Contributors
- [Diletta Rigo](https://github.com/dilettarigo) 
- [Filippo Fantinato](https://github.com/FilippoFantinato)
- [Nicolò Greggio](https://github.com/nicologreggio/)

<br>

---
<br>

## Assignment 1 - Minimum Spanning Tree
### Algorithms
In the first assigment you will compare three algorithms for the Minimum Spanning Tree problem:

- Prim's Algorithm implemented with a Heap
- Naive Kruskal's Algorithm with O(mn) complexity
- Efficient Kruskal's Algorithm based on Union-Find

### Dataset
The dataset contains 68 example graphs, ranging in size from 10 to 100,000 vertices, generated randomly with stanford-algs' TestCaseGenerator. Each file describes an undirected graph with integer weights using the following format:

```
[number_of_nodes] [number_of_edges] 
[one_node_edge_1] [other_node_edge_1] [weight_edge_1] 
[one_node_edge_2] [other_node_edge_2] [weight_edge_2] 
[one_node_edge_3] [other_node_edge_3] [weight_edge_3] 
...
```

For example, a row "2 3 -8874" indicates that there is an edge connecting vertex 2 to vertex 3 with weight -8874. Weights should NOT be assumed to be positive nor distinct.

### Question 1

Run the three algorithms you have implemented (Prim, Kruskal naive and Kruskal efficient) on the graphs of the dataset. Measure the execution times of the three algorithms and create a graph showing the increase of execution times as the number of vertices in the graph increases. Compare the measured times with the asymptotic complexity of the algorithms. For each problem instance, report the weight of the minimum spanning tree obtained by your code.

### Question 2

Comment on the results you have obtained: 
- how do the algorithms behave with respect to the various instances? 
- Is there an algorithm that is always better than the others? 
- Which of the three algorithms you have implemented is more efficient? 

### What to deliver
A brief report on your project. The report must contain: 
- an introductory section with a description of the algorithms and implementation choices you have made;
- explanatory graphs of the results with the answers to the two questions; 
- any originality you introduced in the implementation; 
- a concluding section with your comments and your conclusions on results. 
- The source code of the implementation in a single archive file (.zip, .tar.gz, etc.).

The first assigment must be delivered by Monday 25 April, 11:55 pm. Late submissions get a penalty.

### Final remarks
You can implement the algorithms with any programming language you like. Basic data structures such as lists, queues, stacks, sets, dictionaries or maps, provided by the standard libraries of the language, can be used without restrictions. It is not allowed to use libraries that directly provide data structures and algorithms to represent and manipulate graphs, such as NetworkX, JGraphT or similar. 
Comment the essential parts of the code so that the reader can grasp the ideas that led you to write the code in that way. Comments help to clarify whether a bug is a conceptual error or just a small mistake.

<br>

---
<br>

## Assignment 2 - Traveling Salesman Problem

### General Description
In this assignment you are asked to solve an intractable problem and to compare the execution times and the quality of the solutions that can be obtained with different approximation algorithms. The problem to be analyzed is the "Traveling Salesman Problem" (TSP), defined as follows: given the coordinates x,y ofN points in the plane (the vertices), and a weight function w(u,v) defined for all pairs of points (the arcs), find the simple loop of minimum weight that visits all the N points. The weight function w(u,v) is defined as the Euclidean or Geographic distance between the points u and v (you can find details on how to calculate the distance in the dataset description) . The weight function is symmetric and respects the triangular inequality.

### Algorithms
The algorithms to implement are from two categories: (1) constructive heuristics; and (2) 2-approximate algorithm. 

- Constructive heuristics: choose two of the following constructive heuristics and implement them: Nearest Neighbor, Closest Insertion, Farthest Insertion, Random Insertion, Cheapest Insertion. 
- 2-approximate algorithm: Implement the 2-approximate algorithm based on the minimum spanning tree.

### Dataset

The dataset contains 13 graphs, some from real test cases and some randomly generated. It is a subset of the dataset from TSPLIB and is in the file tsp_dataset.zip.

The first lines of each file contain some information about the instance, such as the number of N points (ranging from 14 to 1000) and the type of coordinates: Euclidean (EUC_2D) or Geographic (GEO). As an example the first lines of eil51.tsp are as follows:
```
NAME : eil51

COMMENT : 51-city problem (Christofides/Eilon)
TYPE : TSP
DIMENSION : 51
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
1 37 52
2 49 49
3 52 64
4 20 26
```

The lines after NODE_COORD_SECTION contain the vertices of the graph: each line includes a vertex ID (unique integer) followed by the x and y coordinates which. The three values are separated by spaces. 

The following table summarizes some statistics of the dataset:

| File |	Description |	N	| Optimal solution
| ---- | ------------ | - | ----------------
| burma14.tsp	 | Burma (Myanmar) | 14 | 3323
| ulysses16.tsp | Mediterranean Sea	| 16 | 6859
| ulysses22.tsp |	 Mediterranean Sea | 22 | 7013
| eil51.tsp |	Synthetic |	51 | 426
| berlin52.tsp | Germany | 52 | 7542
| kroD100.tsp |	Random | 100 | 21294
| kroA100.tsp |	Random | 100 | 21282
| ch150.tsp | Random | 150 | 6528
| gr202.tsp | Europe | 202 | 40160
| gr229.tsp | Asia/Australia | 229 | 134602
| pcb442.tsp | Drilling | 442 | 50778 
| d493.tsp | Drilling	| 493 | 35002
| dsj1000.tsp |	Random | 1000 | 18659688 


### Input handling and distance computation
- **GEO format:** the x coordinate is the latitude, the y coordinate is the longitude
convert x, y coordinates to radians using the code specified in the TSPLIB FAQ (Q: I get wrong distances for problems of type GEO.). The formula uses the integer part of x and y (DOES NOT ROUND TO THE NEAREST INTEGER).
compute the geographic distance between points i and j using the FAQ code for "dij". The code uses the integer part of the distances (does not round).
- **File in EUC_2D format:** No coordinate conversions are needed in this case. Calculate the Euclidean distance and round the value to the nearest integer.

### Question 1
Run the three algorithms (the two constructive heuristics and 2-approximate) on the 13 graphs of the dataset. Show your results in a table like the one below. The rows in the table correspond to the problem instances. The columns show, for each algorithm, the weight of the approximate solution, the execution time and the relative error calculated as

$ \frac{ApproximateSolution−OptimalSolution}{OptimalSolution} $

### Question 2
Comment on the results you have obtained: how do the algorithms behave with respect to the various instances? Is there an algorithm that always manages to do better than the others with respect to the approximation error? Which of the three algorithms you have implemented is more efficient?

### What to deliver
- A brief report on your project. The report must contain: 
  - an introductory section with a description of the algorithms and implementation choices you have made;
  - the table with the results and the answers to the two questions; 
  - any originality you introduced in the implementation; 
  - a concluding section with your comments and your conclusions on results. 
- The source code of the implementation in a single archive file (.zip, .tar.gz, etc.).
### How to submit the assigment
You can do the assigment either on your own or in a group of up to three people. 
You have to create a group even if you do the assigment on your own.
The second assigment must be delivered by Monday 16 May, 11:55 pm. Late submissions get a penalty.
### Final remarks
- You can implement the algorithms with any programming language you like. Basic data structures such as lists, queues, stacks, sets, dictionaries or maps, provided by the standard libraries of the language, can be used without restrictions. It is not allowed to use libraries that directly provide data structures and algorithms to represent and manipulate graphs, such as NetworkX, JGraphT or similar. 
- Comment the essential parts of the code so that the reader can grasp the ideas that led you to write the code in that way. Comments help to clarify whether a bug is a conceptual error or just a small mistake. 

<br>

---
<br>