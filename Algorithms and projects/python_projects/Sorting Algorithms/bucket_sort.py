###########################################
#
# TIME COMPLEXITY:
#  BIG O(n^2)
#  BIG Ω(n + k) 
#  BIG Θ(n)
#
# SPACE COMPLEXITY O(n+k) 
#
###########################################

array = [.24,.26,.43,.15,.41,.47,.52,.80]

def BS(array):
	bucket = []

	for _ in range(int(max(array)*10)+1):
		bucket.append([])

	for i in array:
		idx = int(10*i)
		bucket[idx].append(i)

	for i in range(len(bucket)):
		bucket[i] = sorted(bucket[i])

	k=0

	for i in range(len(bucket)):
		for j in range(len(bucket[i])):
			array[k] = bucket[i][j]
			k+=1
	return array

print(BS(array))