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

array = [327,2,72572,7,3,47,2,8,5]

def BS(array):
	for i in range(len(array)):
		for j in range(len(array)-1-i):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
	return array
print(BS(array))