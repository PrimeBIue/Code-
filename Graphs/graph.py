# implementation of an undirected graph using Adjacency Lists
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = []
	
	def add_neighbor(self, v, weight):
		if v not in self.neighbors:
			self.neighbors.append((v, weight))
			self.neighbors.sort()

class Graph:
	vertices = {}
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			#name to identify easily and vertex object to add neighbors
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v, weight=0):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(v, weight)
			self.vertices[v].add_neighbor(u, weight)
			return True
		else:
			return False
			
	def print_graph(self):
		for i in sorted(list(self.vertices)):
			print(f'{i}: {self.vertices[i].neighbors}')

g = Graph()
# print(str(len(g.vertices)))
#a = Vertex('A')
#g.add_vertex(a)
#g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('F')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB','AC','CD','ED','EC','EB']
for i in edges:
	g.add_edge(i[0], i[1])

g.print_graph()

# print(g.vertices['A'].neighbors)