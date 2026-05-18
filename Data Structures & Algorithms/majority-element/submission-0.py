class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict = {}
        for number in nums:
            dict[number] = dict.get(number,0) + 1
        return max(dict, key=dict.get)