#Dict of list as a connected graph

graph = {'A':['B','C','E'],
         'B':['D','E'],
         'C':['F','G'],
         'D':['B','E'],
         'E':['A','B','D'],
         'F':['C'],
         'G':['C']
         }

print(graph)
visited = []
def traverse_now(visited,graph,node):
    print(visited)
    print(node)
    if node not in visited:
        visited.append(node)
        for each_neighbor in graph[str(node)]:
            traverse_now(visited,graph,each_neighbor)

traverse_now(visited,graph,'A')