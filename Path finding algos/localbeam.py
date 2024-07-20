from heapq import heappush, heappop

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

def heuristic(node, goal):
    return abs(goal - node)

def lbs(graph, start, goal, beam_width):
    pq = []
    heappush(pq, (0, start, [start]))  

    while pq:
        beams = [heappop(pq) for _ in range(min(beam_width, len(pq)))]
        next_beams = []

        for cost, node, path in beams:
            if node == goal:
                return path, cost

            for neighbor, weight in graph.edges.get(node, []):
                new_cost = cost + weight
                new_path = path + [neighbor]
                heappush(next_beams, (new_cost + heuristic(neighbor, goal), neighbor, new_path))
        
        pq = next_beams

    return None, float('inf')
graph = Graph()
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 4, 5)

start = 0
goal = 4
beam_width = 2

path, cost = lbs(graph, start, goal, beam_width)
print(f"Path: {path}, Cost: {cost}")
