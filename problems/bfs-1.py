from queue import Queue
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = Queue()
def dfs():
    while not visited.empty():
        curr = visited.get()
        print("IN ", curr)
        for node in graph[curr]:
            visited.put(node)
            print("Out ", curr)
    
visited.put("A")        
dfs()
