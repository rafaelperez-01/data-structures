
# The first operation (building prefix sum) is O(n) with O(n) space complexity.
# After that, each range sum query is O(1) due to precomputed sums (amortized optimization).
def build_prefix_sum(nums):
    prefix = []
    total = 0
    for n in nums:
        total += n
        prefix.append(total)
    return prefix

def prefixSum(prefix, l, r):
    prefixR = prefix[r]
    prefixL = prefix[l - 1] if l > 0 else 0
    return prefixR - prefixL