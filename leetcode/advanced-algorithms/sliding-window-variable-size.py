

# Time complexity: O(n)
# Space complexity: O(1)
# Q: Find the length of the longest subarray with the same value
# in each position.

def sliding_window_variable_size(nums):
    l = 0
    length = 0
    for r in range(len(nums)):
        if nums[r] != nums[l]:
            l = r
        length = max(length, r - l + 1)
    return length

# Time Complexity: 0(n^2)
# Space Complexity: O(1)
# Q: Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive.
def classic_example(nums):
    l, total = 0, 0
    length = float('inf')
    for r in range(len(nums)):
        total += nums[r]
        while total >= length:
            length = min(r - l, length)
            total -= nums[l]
            l += 1
    return 0 if length == float('inf') else length

