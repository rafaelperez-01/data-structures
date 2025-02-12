

# Time Complexity O(n)
# Space Complexity O(1)
def kadanes(nums):
    curSum = 0
    maxSum = nums[0]
    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


