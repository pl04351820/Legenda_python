def max_heap_sort(nums):
	""" maximum heap sorter
		Time: O(nlog(n))
	"""
	def max_heapify(nums,end):
		last_parent = (end-1) // 2
		# Iterate from last_parent to first
		for parent in range(last_parent, -1, -1):
			current_parent = parent 
			while current_parent <= last_parent:
				child = 2*current_parent + 1
				if child + 1 <= end and nums[child] < nums[child+1]:
					child += 1
				if nums[child] > nums[current_parent]:
					temp = nums[current_parent]
					nums[current_parent] = nums[child]
					nums[child] = temp
					current_parent = child
				else:
					break

	for i in range(len(nums)-1, 0, -1):
		max_heapify(nums, i)
		temp = nums[0]
		nums[0] = nums[i]
		nums[i] = temp
	return nums

print(max_heap_sort([1,3,2,3,5,6,6,72,11,22]))