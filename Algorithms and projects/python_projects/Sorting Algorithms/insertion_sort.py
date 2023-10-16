###########################################
#
# TIME COMPLEXITY:
#  BIG O(n^2)
#  BIG Ω(n) 
#  BIG Θ(n^2)
#
# SPACE COMPLEXITY O(1) 
#
###########################################

array = [2,6,2357,2,44,7,42,1,10,812,58,56]

def IS(array):
	for i in range(len(array)):
		while i > 0 and array[i-1] > array[i]:
			array[i-1], array[i] = array[i], array[i-1]
			i-=1
	return array

print(IS(array))