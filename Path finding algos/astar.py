
from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {
    "/": [(0, ("/","A"))],
"A": [(9, ("A", "B")), (4, ("A", "C")), (7, ("A", "D"))],
"B": [(9, ("B", "A")), (11, ("B", "E"))],
"C": [(4, ("C", "A")), (17, ("C", "E")),(12, ("C", "F"))],
"D": [(7, ("D", "A")), (14, ("D", "F"))],
"E": [(11, ("E", "B")), (17, ("E", "C")), (5, ("E", "Z"))],
"F": [(12, ("F", "C")), (14, ("F", "D")), (9, ("F", "Z"))],
"Z": [(5, ("Z", "E")), (9, ("Z", "F"))]
                            }
        self.edges = {}
        self.weights = {}
        self.heristics = {
            "A" : 21,
            "B" : 14,
            "C" : 18,
            "D" : 18,
            "E" : 5,
            "F" : 8,
            "Z": 0
        }
        self.populate_edges()
        self.populate_weights()
        print("edges : ", self.edges)
        print("weights  : ", self.weights)

    def populate_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
                neighbours.append(each_tuple[1][1])
            self.edges[key] = neighbours

    def populate_weights(self):
        for key in self.graph:
            neighbours = self.graph[key]
            for each_tuple in neighbours:
                self.weights[each_tuple[1]] = each_tuple[0]

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node,  to_node)]

    def get_heuristic(self, node):
        return self.heristics[node]

def astar(graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:
                    g = cost + graph.get_cost(node, i)
                    total_cost = g + graph.get_heuristic(i)
                    queue.put((total_cost, i))
    return visited

print("Traversal : ", astar(Graph(), "A", "Z"))