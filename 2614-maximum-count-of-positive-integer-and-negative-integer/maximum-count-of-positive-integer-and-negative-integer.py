class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def lower_bound(target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        first_non_negative = lower_bound(0)
        first_positive = lower_bound(1)

        neg_count = first_non_negative
        pos_count = len(nums) - first_positive

        return max(neg_count, pos_count)