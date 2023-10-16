###########################################
#
# TIME COMPLEXITY:
#  BIG O(log n) 
#  BIG Ω(1) 
#  BIG Θ(log n)
#
# SPACE COMPLEXITY O(1) 
#
###########################################

array = [1,12,6,2,7,23,4,783,8,]
array = sorted(array)

def BS(array, x):
	lo = 0
	hi = len(array)-1

	while lo <= hi:
		mid = (lo+hi)//2
		if array[mid] == x:
			return True
		if array[mid] < x:
			lo = mid + 1
		if array[mid] > x:
			hi = mid -1
	return False

print(BS(array, 6))

