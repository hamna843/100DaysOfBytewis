from collections import defaultdict, deque
class Graph:


	def __init__(self):

		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):

		visited.add(v)
		print(v, end=' ')


		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)


	def DFS(self, v):

		
		visited = set()


		self.DFSUtil(v, visited)

	def BFS(self, v):
		visited = set()
		queue = deque([v])
		visited.add(v)
		while queue:
			vertex = queue.popleft()
			print(vertex, end=' ')
			for neighbour in self.graph[vertex]:
				if neighbour not in visited:
					visited.add(neighbour)
					queue.append(neighbour)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(" Depth First Traversal")


g.DFS(2)
print(" \n Breadth First Traversal")
g.BFS(2)
