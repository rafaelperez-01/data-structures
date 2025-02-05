# 26. Remove Duplicates from Sorted Array
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l