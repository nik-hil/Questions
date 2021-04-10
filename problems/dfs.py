# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
def dfs(node):
    if node not in visited:
        print(node)
        for n in graph[node]:
            dfs(n)
            
dfs("A")
