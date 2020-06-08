from breadth_first_search import read_graph

def dfs(G, start_node):

	stack = [start_node]
	discovered = {}

	for node in G:
		discovered[node] = False
	discovered[start_node] = True

	dfs_path = []

	while len(stack) > 0:
		v = stack.pop(len(stack) - 1)
		dfs_path.append(v)
		if len(G[v]) != 0:
			for w in G[v]:
				if discovered[w] == False:
					discovered[w] = True
					stack.append(w)


	return dfs_path

def dfs_recurisve(G, start_node, explored, sequence):

	explored[start_node] = True
	for v in G[start_node]:
		if explored[v] == False:
			explored[v] = True
			sequence.append(v)
			dfs_recurisve(G, v, explored, sequence)

def call_dfs_recursive(G, start_node):

	explored = {}
	for node in G:
		explored[node] = False

	sequence = [start_node]
	dfs_recurisve(G, start_node, explored, sequence)

	return sequence

def indegree_graph(G):

	indeg = {}

	for node in G:
		if node not in indeg:
			indeg[node] = 0

		l = G[node]
		for node in l:
			if node not in indeg:
				indeg[node] = 0


	for node in indeg:
		count_in_node = 0
		for node_ in G:
			l = G[node_]
			if node in l:
				count_in_node += 1
		indeg[node] = count_in_node

	return indeg

def topological_sort(G, indeg):

	stack = []
	topological_order = []

	for node in indeg:
		if indeg[node] == 0 and node not in stack:
			stack.append(node)

	#dfs
	while len(stack) > 0:
		u = stack.pop()
		topological_order.append(u)
		if u in G:
			for node in G[u]:
				indeg[node] -= 1
				if indeg[node] == 0:
					stack.append(node)

	return topological_order

'''
filename = 'SCC.txt'
graph = read_graph(filename)
#start_node = choice(list(graph.keys()))
#start_node = 2
#print(call_dfs_recursive(graph, start_node))
indeg = indegree_graph(graph)
print(topological_sort(graph, indeg))
'''

