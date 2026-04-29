class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binary_search(nums1, nums2, i):
            # Goal: Find the most distant pair to the right of i
            left = i
            right = len(nums2)-1

            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] < nums1[i]:
                    right = mid - 1
                elif nums2[mid] >= nums1[i]:
                    left = mid + 1
            return right if nums2[right]>=nums1[i] else -1

        max_distance = 0
        for i in range(len(nums1)):
            j = binary_search(nums1, nums2, i)
            if j != -1:
                max_distance = max(j-i, max_distance)
        return max_distance
# O-O-O-X-X-X-X-X