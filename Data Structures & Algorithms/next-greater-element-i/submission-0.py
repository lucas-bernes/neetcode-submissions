class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            j = nums2.index(num)
            next_greater = -1
            while j<len(nums2):
                if nums2[j] > num: 
                    next_greater = nums2[j]
                    break
                j += 1
            output.append(next_greater)
        return output
