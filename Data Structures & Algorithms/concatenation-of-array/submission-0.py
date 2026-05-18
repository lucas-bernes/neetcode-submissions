class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        k = 0
        while k < 2:
            i=0
            while i<len(nums):
                ans.append(nums[i])
                i+=1
            k+=1

        return ans

        