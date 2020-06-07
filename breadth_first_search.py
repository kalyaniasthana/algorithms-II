from random import choice

def read_graph(filename):

	graph = {}
	with open(filename) as f:
		for line in f:
			line = line.strip('\n')
			line = line.split(' ')
			node_1 = int(line[0])
			node_2 = int(line[1])
			if node_1 not in graph:
				graph[node_1] = []
			graph[node_1].append(node_2)

	return graph


def bfs(G, start_node):

	Q = [] 
	discovered = {}
	for node in G:
		discovered[node] = False
	discovered[start_node] = True
	bfs_path = []

	Q.append(start_node)

	while len(Q) > 0:
		v = Q.pop(0)
		bfs_path.append(v)
		if len(G[v]) != 0:
			#print(len(G[v]))
			for w in G[v]:
				if discovered[w] == False:
					discovered[w] = True
					Q.append(w)

	return bfs_path

filename = 'SCC.txt'
graph = read_graph(filename)
start_node = choice(list(graph.keys()))
print(bfs(graph, start_node))