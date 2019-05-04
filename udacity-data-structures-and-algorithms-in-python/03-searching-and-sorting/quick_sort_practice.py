"""Implement quick sort in Python.
Input a list.
Output a sorted list.

Example:
>>> array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
>>> print(quicksort(array, 0, len(array) - 1))
[1, 3, 4, 6, 9, 14, 20, 21, 21, 25]
"""

def partition(arr, start, end):
	# Repeat until partition has one item
    # due to in-place sorting, we can use 
    # start, end instead of len(list)
    pivot = end
    wall = start
    i = start
    while i < pivot:
	    # Move elements smaller than pivot 
	    # to the left of wall. Wall then
	    # moves right.
	    if arr[i] < arr[pivot]:
	    	arr[i], arr[wall] = arr[wall], arr[i]
	    	wall += 1
	    i += 1
	# Finally pivot swap with wall so that 
	# elements smaller than pivot is left 
	# of pivot, and elements greater or 
	# equal to pivot is right of pivot.
    arr[pivot], arr[wall] = arr[wall], arr[pivot]
    return wall		

def quicksort(arr, start, end):
	if start < end:
		pivot = partition(arr, start, end)
		# Sort the partions before and after
		# the pivot recursively
		quicksort(arr, start, pivot - 1)
		quicksort(arr, pivot + 1, end)
	return arr

if __name__ == '__main__':
	import doctest
	doctest.testmod()