class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return 0.
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2)//2]+nums2[len(nums2)//2-1]) / 2.
            else:
                return float(nums2[len(nums2)//2])
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1]) / 2.
            else:
                return float(nums1[len(nums1)//2])
        total = len(nums1) + len(nums2)
        median = 0.
        i, j = 0, 0
        picked = 0
        if total % 2 == 0:
            while picked<total:
                picked += 1
                if i == len(nums1):
                    if picked == total//2:
                        median += nums2[j]
                    if picked == total//2+1:
                        median += nums2[j]
                        return median/2
                    j += 1
                    continue
                if j == len(nums2):
                    if picked == total//2:
                        median += nums1[i]
                    if picked == total//2+1:
                        median += nums1[i]
                        return median/2
                    i += 1
                    continue
                if nums1[i] <= nums2[j]:
                    if picked == total//2:
                        median += nums1[i]
                    if picked == total//2+1:
                        median += nums1[i]
                        return median/2
                    i += 1
                else:
                    if picked == total//2:
                        median += nums2[j]
                    if picked == total//2+1:
                        median += nums2[j]
                        return median/2
                    j += 1
            return 0.
        else:
            while picked<total:
                picked += 1
                if i == len(nums1):
                    if picked == total//2+1:
                        median += nums2[j]
                        return median
                    j += 1
                    continue
                if j == len(nums2):
                    if picked == total//2+1:
                        median += nums1[i]
                        return median
                    i += 1
                    continue
                if nums1[i] <= nums2[j]:
                    if picked == total//2+1:
                        median += nums1[i]
                        return median
                    i += 1
                else:
                    if picked == total//2+1:
                        median += nums2[j]
                        return median
                    j += 1
            return 0.