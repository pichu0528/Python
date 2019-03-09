'''
Given 
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
Note: the vertices is in a set
'''

def bfs(graph,start):
    visited = set()
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        
        if vertex not in visited:
            visited.add(vertex)
            
            queue.extend(graph[vertex] - visited)
            
    return visited
    
'''
Given
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
         
Note: the vertices are in a list
'''
def bfs(graph,start):
    visited = []
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        
        if vertex not in visited:
            visited.append(vertex)
            
            queue.extend([v for v in graph[vertex] if v not in visited])
            
    return visited
