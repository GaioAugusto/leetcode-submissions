class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter, result = 0, 0

        for num in nums:
            if counter == 0:
                result = num
            if result == num:
                counter += 1
            else:
                counter -= 1
        return result