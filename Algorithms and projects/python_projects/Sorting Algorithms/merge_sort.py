###########################################
#
# TIME COMPLEXITY:
#  BIG O(n*log n)
#  BIG Ω(n*log n) 
#  BIG Θ(n*log b)
#
# SPACE COMPLEXITY O(n) 
#
###########################################

array = [2,72,7,48,2,892,2,422,484,912,1,0]


def MS(array):
	if len(array) > 1:
		mid = len(array)//2
		left = array[:mid]
		right = array[mid:]

		MS(left)
		MS(right)

		i = j = k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i+=1
			else:
				array[k] = right[j]
				j+=1
			k+=1

		while i < len(left):
			array[k] = left[i]
			i+=1
			k+=1

		while j < len(right):
			array[k] = right[j]
			j+=1
			k+=1
	return array

print(MS(array))