# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i1 = 0
        i2 = 0
        while (i1 < len(nums1) or i2 < len(nums2)):
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] < nums2[i2]:
                    merged.append(nums1[i1])
                    i1 += 1
                else:
                    merged.append(nums2[i2])
                    i2 += 1
            elif i1 < len(nums1) and i2 >= len(nums2):
                merged += nums1[i1:]
                break
            else:
                merged += nums2[i2:]
                break
        if len(merged) % 2 == 0:
            return (merged[int(len(merged)/2) - 1] + merged[int(len(merged)/2)])/2
        else:
            return merged[int(len(merged)/2)]