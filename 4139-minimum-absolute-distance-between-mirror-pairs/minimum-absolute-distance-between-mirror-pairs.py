class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(n):
            result = 0
            while n > 0:
                result = result*10 + n % 10
                n = n // 10
            return result

        value_index = {}
        current_min = len(nums)
        pair_exist = False
        for j in range(len(nums)):
            if nums[j] in value_index:
                pair_exist = True
                if j - value_index[nums[j]] < current_min:
                    current_min = j - value_index[nums[j]]
            value_index[reverse(nums[j])] = j
        return current_min if pair_exist else -1