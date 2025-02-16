
# Time complexity O(n)
# Space complexity O(k)
def closeDuplicates(nums, k):
    window = set() # cur window of size <= k
    l, r = 0, 0
    for r in range(len(nums)):
        if r - l + 1 > k:
            window.remove(nums[r])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])
    return False