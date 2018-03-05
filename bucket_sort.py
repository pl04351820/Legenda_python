import math
def bucket_sort(nums, Bucket_Size = 1):
	""" Bucket sort with size 5
	"""
	if len(nums) < 2: return nums
	# Decide the size of bucket
	minvalue = nums[0]
	maxvalue = nums[0]
	for i in range(1,len(nums)):
		if nums[i] > maxvalue:
			maxvalue = nums[i]
		elif nums[i] < minvalue:
			minvalue = nums[i]

	# Initialize Bucket
	bucket_count = math.floor(abs(maxvalue - minvalue) / Bucket_Size) + 1
	bucket = []
	for i in range(bucket_count):
		bucket.append([])

	# Distribute input to bucket
	for i in range(len(nums)):
		bucket[math.floor((nums[i] - minvalue) / Bucket_Size)].append(nums[i])

	# Sort bucket and place it back
	nums = []
	for i in range(bucket_count):
		bucket[i].sort()
		for j in range(len(bucket[i])):
			nums.append(bucket[i][j])
			
	return nums

print(bucket_sort([1,3,2,1,6,8,4,3,3]))