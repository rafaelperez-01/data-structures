# 1929. Concatenation of Array
# Time complexity: O(n)
# Space complexity: O(n)

def ConcatenationOfArray(nums):
    n = len(nums)
    ans = [0] * (n * 2)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans


