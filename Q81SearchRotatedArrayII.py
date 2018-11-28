class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return nums[0] == target
        i = 0
        while i<len(nums)-1:
            if nums[i+1] < nums[i]:
                break
            i += 1
        nums1, nums2 = nums[:i+1], nums[i+1:]
        if len(nums2) and target <= nums2[-1]:
            l, r = 0, len(nums2)
            while l < r:
                mid = (l+r) // 2
                if target < nums2[mid]:
                    r = mid
                elif target > nums2[mid]:
                    l = mid+1
                else:
                    return True
            return False
        elif target <= nums1[-1]:
            l, r = 0, len(nums1)
            while l < r:
                mid = (l+r) // 2
                if target < nums1[mid]:
                    r = mid
                elif target > nums1[mid]:
                    l = mid+1
                else:
                    return True
            return False
        else:
            return False