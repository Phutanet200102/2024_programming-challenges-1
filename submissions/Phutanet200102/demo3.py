import heapq
import re
from collections import defaultdict


def dijkstra(edges, start, end):
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))
    
    queue = [(0, start)]
    distances = {start: 0}
    visited = set()
    
    while queue:
        current_distance, node = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == end:
            return current_distance
        
        for weight, neighbor in graph[node]:
            distance = current_distance + weight
            
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return float('inf')

def parse_edges(edges_input):
    edge_pattern = re.compile(r'\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)')
    edges = []
    for match in edge_pattern.finditer(edges_input):
        u, v, weight = map(int, match.groups())
        edges.append((u, v, weight))
    return edges

def main():
    edges_input = input("Input edges as (node1, node2, weight): ")
    start = int(input("Input the start node: "))
    end = int(input("Input the end node: "))
    
    edges = parse_edges(edges_input)
    
    shortest_distance = dijkstra(edges, start, end)
    print(f"Output: {shortest_distance}")

if __name__ == "__main__":
    main()
