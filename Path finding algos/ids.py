class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

def depth_limited_search(graph, current_node, goal, limit, path, cost):
    if current_node == goal:
        return path, cost

    if limit <= 0:
        return None, float('inf')

    for neighbor, weight in graph.edges.get(current_node, []):
        result, result_cost = depth_limited_search(graph, neighbor, goal, limit - 1, path + [neighbor], cost + weight)
        if result is not None:
            return result, result_cost

    return None, float('inf')

def iterative_deepening_search(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        path, cost = depth_limited_search(graph, start, goal, depth, [start], 0)
        if path is not None:
            return path, cost

    return None, float('inf')

# Example usage:
graph = Graph()
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 4, 5)

start = 0
goal = 4
max_depth = 5

path, cost = iterative_deepening_search(graph, start, goal, max_depth)
print(f"Path: {path}, Cost: {cost}")
