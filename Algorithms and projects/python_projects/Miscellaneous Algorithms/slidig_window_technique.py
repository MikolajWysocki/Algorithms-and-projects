array = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

#looking for max sum
def MS(array, k):
	n = len(array)

	if n < k:
		return -1

	curr_sum = sum(array[:k])
	max_sum = curr_sum

	for i in range(n-k):
		curr_sum = curr_sum - array[i] + array[i+k]
		max_sum = max(max_sum, curr_sum)
	return max_sum

print(MS(array, k))