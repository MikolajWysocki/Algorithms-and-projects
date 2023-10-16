###########################################
#
# TIME COMPLEXITY:
#  BIG O(n^2) 
#  BIG Ω(n^2) 
#  BIG Θ(n^2)
#
# SPACE COMPLEXITY O(1) 
#
###########################################

array = [2,756,24,7,82,4,8,24,885,3,53]

def SS(array):
	for i in range(len(array)):
		min_idx = i
		for j in range(i+1, len(array)):
			if array[j] < array[min_idx]:
				min_idx = j
		if min_idx != i:
			array[i], array[min_idx] = array[min_idx], array[i]
	return array

print(SS(array))