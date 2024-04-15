"""
Rotate array clockwise / right
"""
class RotateArray:
	def rotateArray(self, nums, steps):
		steps = steps % len(nums)
		
		#If the given steps is a negative value
		if steps < 0:
			steps += len(nums)
			
		self.reverseArray(nums, 0, len(nums) - 1)
		self.reverseArray(nums, 0, steps - 1)
		self.reverseArray(nums, steps, len(nums) - 1)
		
		return nums
		
	def reverseArray(self, array, leftIndex, rightIndex):
		while(leftIndex <= rightIndex):
			temp = array[leftIndex]
			array[leftIndex] = array[rightIndex]
			array[rightIndex] = temp
			
			leftIndex += 1
			rightIndex -= 1
			
		return array
			
