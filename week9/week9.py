# Example of a Breath First Algorithm
graph = {
  'Jannie' : ['Charlie'],
  'Charlie' : ['Jannie', 'Else', 'Helge'],
  'Else' : ['Charlie'],
  'Helge' : ['Charlie', 'Hanne'],
  'Hanne' : ['Helge', 'Frederik','Ayse'],
  'Frederik' : ['Hanne'],
  'Ayse': ['Hanne', 'Holger'],
  'Holger': ['Ayse', 'Hans'],
  'Hans': ['Holger']
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
    counter = 0
    visited.append(node)
    queue.append(node)

    while queue: # while the list is not empty
        s = queue.pop(0) 
        print(f'{counter} {s}\n') # end = (default is \n)
        counter+= 1
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code



# Traverse and print each node plus sequence number of the node in the traversal of the below graph:
# Create a function that can take a name and show all employees that are in the hierarchy of that supervisor. E.g Helge has all others, Charlie has Jannie and Else, etc.


if __name__ == "__main__":
    bfs(visited, graph, 'Jannie')