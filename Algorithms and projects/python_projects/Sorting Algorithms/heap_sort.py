###########################################
#
# TIME COMPLEXITY:
#  BIG O(n*log n)
#  BIG Ω(n*log n) 
#  BIG Θ(n*log n)
#
# SPACE COMPLEXITY O(1) 
#
###########################################

array = [1,56,37,2,8,2,8,9,9,666,3]

def Heapify(array, n, i):
	largest = i
	l = 2*i+1
	r = 2*i+2

	if l < n and array[l] > array[largest]:
		largest = l
	if r < n and array[r] > array[largest]:
		largest = r

	if largest != i:
		array[i], array[largest] = array[largest], array[i]
		Heapify(array, n, largest)

def HS(array):
	n = len(array)
	for i in range(n//2, -1, -1):
		Heapify(array, n, i)

	for i in range(n-1, 0, -1):
		array[i], array[0] = array[0], array[i]
		Heapify(array, i, 0)
	return array

print(HS(array))