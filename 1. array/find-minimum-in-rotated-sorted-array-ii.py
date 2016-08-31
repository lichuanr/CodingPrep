1, this question tests us the edge cases. 
worset case [1, 1, 1, 1, 1] -> O(N)
 - In the worset case, binary search is same time complexity as the linear search

Best case [2, 3, 4, 0, 1] -> O(logN)


2, Implentation:
compare the value of mid & end index, then define the range of the lowest value and cut the array by half for the next round of search


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end)/2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid 
            else:
                end -= 1
        
        return nums[start]


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        minNum = nums[0]
        for item in nums:
            if item < minNum:
                minNum = item
        return minNum
