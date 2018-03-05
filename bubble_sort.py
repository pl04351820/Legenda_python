"""
Worst-case performance: O(N^2)
"""
def bubble_sort(nums):
	flag = True
	while flag:
		flag = False
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				temp = nums[i]
				nums[i] = nums[i+1]
				nums[i+1] = temp
				flag = True
	return nums

print(bubble_sort([1,3,2,4,6,2,3,5,1,6,7,3,1]))