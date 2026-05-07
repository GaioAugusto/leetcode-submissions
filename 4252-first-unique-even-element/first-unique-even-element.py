from collections import OrderedDict
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        seen = OrderedDict()

        for num in nums:
            if num % 2 == 0:
                if num in seen:
                    seen[num] += 1
                else:
                    seen[num] = 1
        
        while len(seen) > 0:
            x = seen.popitem(last=False)
            if x[1] == 1:
                return x[0]
        return -1

        