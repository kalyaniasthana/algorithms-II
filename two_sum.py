import sys
from min_heap import read_list
import threading

def array_to_hashtable(array):

	hash_table = {}
	for element in array:
		hash_table[element] = False

	return hash_table
'''
def two_sum_algorithm(hash_table, target, array):

	for element in array:
		complement = target - element
		if complement in hash_table and complement != element:
			return True

	return False

def two_sum_loop(array):

	targets = [i for i in range(-10000, 10001)]
	hash_table = array_to_hashtable(array)

	total = 0

	for target in targets:
		print(total)
		if two_sum_algorithm(hash_table, target, array):
			total += 1

	return total

'''

def two_sum_using_list(array):

	array.sort()
	start = 0
	end = len(array) - 1
	found = array_to_hashtable(array)
	min = -10000
	max = 10000

	while start < end:
		sum = array[start] + array[end]
		if sum < min:
			start += 1
		elif sum > max:
			end -= 1
		else:
			if array[start] != array[end]:
				found[sum] = True
			current_start = start
			current_end = end

			while True:
				start += 1
				sum = array[start] + array[end]
				if sum < min:
					break
				elif sum > max:
					break
				else:
					if array[start] != array[end]:
						found[sum] = True

			start = current_start

			while True:
				end -= 1
				sum = array[start] + array[end]
				if sum < min:
					break
				elif sum > max:
					break
				else:
					if array[start] != array[end]:
						found[sum] = True

			end = current_end
			start += 1
			end -= 1

	count = 0
	for element in found:
		if found[element]:
			count += 1

	return count

def main():

	filename = 'two_sum_numbers.txt'
	array = read_list(filename)
	array = list(set(array))
	print(two_sum_using_list(array))

if __name__ == '__main__':

	main()




