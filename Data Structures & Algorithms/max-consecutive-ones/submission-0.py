class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_sequence = 0
        temp_sequence = 0
        for number in nums:
            if number == 1: 
                temp_sequence += 1
            else:
                temp_sequence = 0
            max_sequence = max(max_sequence, temp_sequence)
        return max_sequence