import heapq

def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    costtillnow = {start: 0}
    
    camefrom = {start: None}
    
    while priority_queue:
        currentcost, currentnode = heapq.heappop(priority_queue)
        
        if currentnode == goal:
            break
        
        for neighbor, weight in graph[currentnode]:
            new_cost = currentcost + weight
            if neighbor not in costtillnow or new_cost < costtillnow[neighbor]:
                costtillnow[neighbor] = new_cost
                priority_queue.append((new_cost, neighbor))
                camefrom[neighbor] = currentnode
    
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = camefrom[node]
    path.reverse()
    
    return path, costtillnow[goal]

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

path, cost = ucs(graph, 'A', 'D')
print("Path:", path)
print("Cost:", cost)
