class Solution:
    def subarraySum(self, nums, k):
        curr_sum = 0
        prefix = {0: 1}
        count = 0
        for num in nums:
            curr_sum += num
            count += prefix.get(curr_sum - k, 0)   # check first
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1  # then insert
        return count