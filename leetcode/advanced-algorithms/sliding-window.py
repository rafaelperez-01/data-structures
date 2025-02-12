
# Time complexity O(n)
# Space complexity O(1)
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    l = 0
    for r in nums:
        if curSum < 0:
            curSum = 0
            l = r
        curSum += r
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = l, r
    return [maxL, maxR]
