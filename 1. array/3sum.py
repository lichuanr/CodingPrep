class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i, item in enumerate(nums):
            if nums[i] == nums[i-1] and i != 0:
                continue
            target = - item
            start, end = i + 1, len(nums) - 1
            while start < end:
                total = nums[start] + nums[end]
                if total > target:
                    end -= 1
                elif total < target:
                    start +=1
                else:
                    result.append([item, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1] :
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
        return  result