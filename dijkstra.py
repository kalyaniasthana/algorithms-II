import sys

def read_dijkstra_graph(filename):

	graph = {}
	weights = {}

	with open(filename, 'r') as f:
		for line in f:
			line = line.strip('\n')
			line = line.strip('\r')
			line = line.split('\t')
			v = int(line[0])
			graph[v] = []
			weights[v] = []
			for i in range(1, len(line) - 1):
				node = line[i].split(',')
				graph[v].append(int(node[0]))
				weights[v].append(int(node[1]))

	return graph, weights

def shortest_path(G, weights, source):

	Q = []
	dist = {}

	for vertex in G:
		dist[vertex] = float('Inf')
		Q.append(vertex)

	dist[source] = 0

	while Q:

		distances = []
		vertices = []

		for v in Q:
			distances.append(dist[v])
			vertices.append(v)

		min_element = min(distances)
		index_of_min_element = distances.index(min_element)
		u = vertices[index_of_min_element]

		Q.remove(u)

		for i in range(len(G[u])):
			neighbor = G[u][i]
			alt = dist[u] + weights[u][i]
			if alt < dist[neighbor]:
				dist[neighbor] = alt

	return dist


filename = 'dijkstraData.txt'
G, weights = read_dijkstra_graph(filename)
dist = shortest_path(G, weights, 1)
nodes = [7,37,59,82,99,115,133,165,188,197]
for node in nodes:
	print(dist[node])
