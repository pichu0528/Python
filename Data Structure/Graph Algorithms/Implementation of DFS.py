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

def dfs(graph,start):
    # all visited vertices are put in the set
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            
            # the subtract is only available for sets
            stack.extend(graph[vertex] - visited)
            
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
def dfs(graph,start):
    # all visited vertices are put in the list
    visited = []
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.append(vertex)
            
            stack.extend([v for v in graph[vertex] if v not in visited])
            
    return visited
