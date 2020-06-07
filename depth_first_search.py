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

'''
filename = 'SCC.txt'
graph = read_graph(filename)
#start_node = choice(list(graph.keys()))
start_node = 2
print(dfs(graph, start_node))
'''