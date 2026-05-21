class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = 1
        integers_not_present = []
        while(x<=len(nums)):
            if x not in nums:
                integers_not_present.append(x)
            x += 1
        return integers_not_present