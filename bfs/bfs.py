"""
Breadth First Search (BFS) for a Graph

We need to account for cycles, where nodse point back to each other.
To avoid processing a node more than once, we use another datastrucutre to track visited nodes.

In this example the graph is structured as a dictionary of lists
{
    1: [2,3,4,5],
    2: [3,4,5],
    3: [4,5],
    4: [5],
    5: [1,2,3,4]
}

Our BFS function:
1. requires a starting node.
2. uses two datastructures: 1) a list of same length of nodes to hold True/False flags; 2) queue for traversal
3. With the queue we can keep track of the nodes to be traversed
4. For the queue, we pop the first item and then we check if the children nodes have been visited, if not we add to queue and switch the flag.

"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,v,u):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

"""

1. requires a matrix; starting point or for loop to start BFS search
2. uses set to keep track of visited points
3. uses queue to progress the search
4. there are conditionals for the search; only process if it hasn't been visited

"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def BFS(self, matrix):
        matrix_row_total = len(matrix)
        matrix_col_total = len(matrix[0])
        
        visited = set()
        queue = []
        starting_point = [0,0] # can be any point, or even searching for different points

        queue.append(starting_point)

        while queue:
            s = queue.pop(0)

            if s not in visited:
                visited.add(s)

                # Action phase, do something, change things, manipulate things, calcuate, etc.
                print(s, "do something")
                print(matrix[s[0]][s[1]])

                if s[0] > 0:    
                    queue.add([s[0]-1, s[1]])
                if s[0] < matrix_row_total:
                    queue.add([s[0]+1, s[1]])
                if s[1] > 0:
                    queue.add([s[0], s[1] - 1])
                if s[1] < matrix_col_total:
                    queue.add([s[0], s[1] + 1])
            else:
                continue