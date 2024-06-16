def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
        min_distance = float('inf')
        next_node = None
        
        for node in graph:
            if node not in visited:
                if distances[node] < min_distance:
                    min_distance = distances[node]
                    next_node = node
        
        visited.add(next_node)
        
        for neighbor, weight in graph[next_node].items():
            distance = distances[next_node] + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances


graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}}
start_node = 'A'
print(dijkstra(graph, start_node))  