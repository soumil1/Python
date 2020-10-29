"""
Optimized approach to bubble sorting algorithm.
It is found that even if an array is sorted, the algorithm keeps traversing the array which increases the time taken.
To avoid this, we can keep a record that if an array has all elements in order, exit the algorithm as it is not needed.
"""
def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		flag = False
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				flag = True
				arr[j], arr[j+1] = arr[j+1], arr[j]
		if not flag:
			break
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)