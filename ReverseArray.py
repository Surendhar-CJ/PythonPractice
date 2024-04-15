from typing import List

class ReverseArray:
	def reverseArray(self, nums: List[int]) -> List[int]:
		left = 0
		right = len(nums) - 1
		
		while (left <= right):
			temp = nums[left]
			nums[left] = nums[right]
			nums[right] = temp
			
			left += 1
			right -= 1

		return nums


if __name__ == "__main__":
	reverse = ReverseArray()
	result = reverse.reverseArray([2,5,6,7,9,345,3246,65476,3,3])
	print(result)
		
