import sys
import resource
#sys.setrecursionlimit(10000000)
#resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
#sys.setrecursionlimit(0x100000)

def read_kosaraju_graph(filename, n):

	graph = [[] for x in range(n)]
	reverse_graph = [[] for x in range(n)]

	with open(filename, 'r') as f:

		for line in f:

			line = line.strip('\n')
			line = line.split(' ')
			node_1, node_2 = int(line[0]) - 1, int(line[1]) - 1
			#print(node_1, node_2)
			graph[node_1].append(node_2)
			reverse_graph[node_2].append(node_1)

	return graph, reverse_graph

def dfs_second_pass(G, start_node):

	stack = [start_node]
	global discovered
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
def dfs_first_pass(G, n):

	global t
	global explored
	global f

	explored = [False for x in range(n)]
	#leader = [0 for x in range(n)]
	f = [0 for x in range(n)]
	#s = None
	t = 0

	for i in range(n-1, -1, -1):
		print(i)
		if explored[i] == False:
			stack = [i]

		print(stack)
		while len(stack) > 0:
			v = stack.pop(len(stack) - 1)
			done = True
			if len(G[v]) != 0:
				for w in G[v]:
					if explored[w] == False:
						explored[w] = True
						stack.append(w)
						done = False
			if done == True:
				f[i] = t
				t += 1

'''

def dfs_recurisve(G, i):

	global explored
	explored[i] = True
	#global leader
	#leader[i] = s
	for v in G[i]:
		if not explored[v]:
			explored[v] = True
			dfs_recurisve(G, v)

	global t
	global f
	f[i] = t
	t += 1
	#print(f)

def dfs_loop(G, n):

	global t
	t = 0

	#global s
	#s = None

	global explored
	explored = [False for x in range(n)]

	global f
	f = [0 for x in range(n)]

	#global leader
	#leader = [0 for x in range(n)]

	for i in range(n-1, -1, -1):
		if not explored[i]:
			#s = i
			dfs_recurisve(G, i)


def kosaraju_second_pass(G, f, n):

	temp_G = [[] for i in range(n)]

	for i in range(n):
		for j in range(len(G[i])):
			x = G[i][j]
			temp_G[i].append(f[x])

	del G
	new_G = [[] for i in range(n)]

	for i in range(n):
		new_G[f[i]] = temp_G[i]

	del temp_G
	global discovered

	all_scc = []

	discovered = [False for i in range(n)]
	for i in range(n-1, -1, -1):
		if not discovered[i]:
			all_scc.append(len(dfs_second_pass(new_G, i)))

	del new_G
	del discovered

	all_scc.sort(reverse = True)

	return all_scc

filename = 'small_test_case.txt'
n = 9
G, G_rev = read_kosaraju_graph(filename, n)
dfs_loop(G_rev, n)
#print(f)
#sys.exit()
#print(G)
del G_rev
#del leader
del explored
#del s
del t
print(kosaraju_second_pass(G, f, n))