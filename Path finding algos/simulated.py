import math
import random

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

def heuristic(node, goal):
    return abs(goal - node)

def simulated_annealing(graph, start, goal, initial_temp, cooling_rate, stopping_temp):
    current_node = start
    current_cost = 0
    current_path = [start]
    
    temperature = initial_temp

    while temperature > stopping_temp:
        neighbors = graph.edges.get(current_node, [])
        if not neighbors:
            return None, float('inf')  # No path to the goal
        
        next_node, next_cost = random.choice(neighbors)
        delta_e = heuristic(next_node, goal) - heuristic(current_node, goal)
        
        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / temperature):
            current_node = next_node
            current_cost += next_cost
            current_path.append(current_node)
        
        temperature *= cooling_rate
        print(f"Current Node: {current_node}, Path: {current_path}, Temperature: {temperature}")

    if current_node == goal:
        return current_path, current_cost
    else:
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
initial_temp = 1000
cooling_rate = 0.95  # Increased the cooling rate
stopping_temp = 0.1  # Lower stopping temperature

path, cost = simulated_annealing(graph, start, goal, initial_temp, cooling_rate, stopping_temp)
print(f"Path: {path}, Cost: {cost}")
