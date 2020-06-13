import sys
from copy import deepcopy

def read_list(filename):

	l = []
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip('\n')
			l.append(int(line))

	return l

#some functions are from https://towardsdatascience.com/data-structure-heap-23d4c78a6962
def min_heapify(array, i):

	left = 2 * i + 1
	right = 2 * i + 2
	length = len(array) - 1
	smallest = i

	if left <= length and array[i] > array[left]:
	    smallest = left

	if right <= length and array[smallest] > array[right]:
	    smallest = right

	if smallest != i:
	    array[i], array[smallest] = array[smallest], array[i]
	    min_heapify(array, smallest)

def max_heapify(array, i):

	left = 2 * i + 1
	right = 2 * i + 2
	length = len(array) - 1
	largest = i

	if left <= length and array[i] < array[left]:
		largest = left

	if right <= length and array[largest] < array[right]:
		largest = right

	if largest != i:
		array[i], array[largest] = array[largest], array[i]
		max_heapify(array, largest)

def build_min_heap(array):

	for i in reversed(range(len(array)//2)):
		min_heapify(array, i)


def build_max_heap(array):

	for i in reversed(range(len(array)//2)):
		max_heapify(array, i)

def heapsort_acsending(array):

    array = deepcopy(array)
    build_min_heap(array)
    sorted_array = []

    for x in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)

    return sorted_array

def heapsort_descending(array):

	array = deepcopy(array)
	build_max_heap(array)
	sorted_array = []

	for x in range(len(array)):
		array[0], array[-1] = array[-1], array[0]
		sorted_array.append(array.pop())
		max_heapify(array, 0)

	return sorted_array

#https://towardsdatascience.com/data-structure-heap-23d4c78a6962 till here

def insert_into_min_heap(heap, element):

	heap.append(element)
	build_min_heap(heap)

def insert_into_max_heap(heap, element):

	heap.append(element)
	build_max_heap(heap)

def extract_min_from_min_heap(heap):

	m = heap[0]
	del heap[0]
	build_min_heap(heap)

def extract_max_from_max_heap(heap):

	m = heap[0]
	del heap[0]
	build_max_heap(heap)

def median_maintenance(stream):

	median = 0

	hlow_max_heap = []
	hhigh_min_heap = []

	hlow_size = 0
	hhigh_size = 0

	sum_of_medians = 0

	for element in stream:

		#print(median, element)
		#print(hlow_size, hhigh_size)
		#print(hlow_max_heap)
		#print(hhigh_min_heap)

		if element < median:
			insert_into_max_heap(hlow_max_heap, element)
		else:
			insert_into_min_heap(hhigh_min_heap, element)

		hlow_size = len(hlow_max_heap)
		hhigh_size = len(hhigh_min_heap)

		if abs(hlow_size - hhigh_size) > 1:
			if hlow_size > hhigh_size:
				#m = max(hlow_max_heap)
				max_value = hlow_max_heap.pop(0)
				#print(m, max_value, 'hlow')
				build_max_heap(hlow_max_heap)
				insert_into_min_heap(hhigh_min_heap, max_value)
			else:
				#m = min(hhigh_min_heap)
				min_value = hhigh_min_heap.pop(0)
				#print(m, min_value, 'hhigh')
				build_min_heap(hhigh_min_heap)
				insert_into_max_heap(hlow_max_heap, min_value)

			hlow_size = len(hlow_max_heap)
			hhigh_size = len(hhigh_min_heap)

		if hlow_size == hhigh_size:
			median = hlow_max_heap[0]

		else:
			if hlow_size > hhigh_size:
				median = hlow_max_heap[0]
			else:
				median = hhigh_min_heap[0]

		sum_of_medians += median

	return sum_of_medians%10000

filename = 'median.txt'
array = read_list(filename)
print(median_maintenance(array))
