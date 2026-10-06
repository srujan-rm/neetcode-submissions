import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (n > m):
            return(self.findMedianSortedArrays(nums2, nums1))
        split = math.ceil((m + n) / 2)
        minimum_taking, maximum_taking = split - n, split
        lp, rp = minimum_taking, maximum_taking
        while (lp <= rp):
            mid = lp + ((rp - lp) // 2)
            left_top = nums1[mid - 1] if mid - 1 < m and mid - 1 >= 0 else float("-inf")
            right_top = nums1[mid] if mid < m and mid >= 0 else float("inf") 
            left_bottom = nums2[split - mid - 1] if split - mid - 1 < n and split - mid - 1 >= 0 else float("-inf")
            right_bottom = nums2[split - mid] if split - mid < n and split - mid >= 0 else float("inf")
            if (left_top <= right_bottom and left_bottom <= right_top):
                if (m + n - split == split):
                    return (max(left_top, left_bottom) + min(right_top, right_bottom))/2 
                else:
                    return(max(left_top, left_bottom))
            elif (left_top > right_bottom):
                rp = mid - 1
            else:
                lp = mid + 1
        return 0.0