class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m == 0:
            if n == 0:
                return 0
            return (nums2[(n - 1) // 2] + nums2[n // 2]) / 2
        if n == 0:
            return (nums1[(m - 1) // 2] + nums1[m // 2]) / 2
        if m >= n:
            left, right = 0, 2 * n
            while left < right:
                mid = (left + right) // 2
                if nums1[(m + n - 1 - mid) // 2] == nums2[mid // 2]:
                    return nums2[mid // 2]
                if nums1[(m + n - 1 - mid) // 2] < nums2[mid // 2]:
                    right = mid
                else:
                    left = mid + 1
            if left == 0:
                if m == n:
                    return (nums1[-1] + nums2[0]) / 2
                return (nums1[(m + n - 1) // 2] + nums1[(m + n) // 2]) / 2
            if left == 2 * n:
                if m == n:
                    return (nums1[0] + nums2[-1]) / 2
                return (nums1[(m - n - 1) // 2] + nums1[(m - n) // 2]) / 2
            return (max(nums1[(m + n - 1 - left) // 2], nums2[(left - 1) // 2]) + min(nums1[(m + n - left) // 2], nums2[left // 2])) / 2

        left, right = 0, 2 * m
        while left < right:
            mid = (left + right) // 2
            if nums1[mid // 2] == nums2[(m + n - 1 - mid) // 2]:
                return nums1[mid // 2]
            if nums1[mid // 2] > nums2[(m + n - 1 - mid) // 2]:
                right = mid
            else:
                left = mid + 1
        if left == 0:
            return (nums2[(m + n - 1) // 2] + nums2[(m + n) // 2]) / 2
        if left == 2 * m:
            return (nums2[(m - n - 1) // 2] + nums2[(m - n) // 2]) / 2
        return (max(nums1[(left - 1) // 2], nums2[(m + n - 1 - left) // 2]) + min(nums1[left // 2], nums2[(m + n - left) // 2])) / 2
