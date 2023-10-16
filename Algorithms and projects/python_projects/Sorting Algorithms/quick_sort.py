###########################################
#
# TIME COMPLEXITY:
#  BIG O(n^2)
#  BIG Ω(n*log n) 
#  BIG Θ(n*log n)
#
# SPACE COMPLEXITY O(log n) 
#
###########################################

array = [2,7,32,823,4384,2,8,2,99,1,0]

def QS(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array.pop()

	smaller = []
	greater = []

	for i in array:
		if i < pivot:
			smaller.append(i)
		if i > pivot:
			greater.append(i)
	return QS(smaller) + [pivot] + QS(greater)

print(QS(array))