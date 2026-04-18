class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def check(mid, nums):
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            return count > mid
        
        # Se o numero de numeros >= que mid for maior que mid

        low = 0
        high = len(nums)-1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid, nums):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans