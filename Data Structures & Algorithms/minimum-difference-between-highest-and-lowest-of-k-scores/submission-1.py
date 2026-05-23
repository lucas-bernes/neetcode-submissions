class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = left+k-1
        minimum = math.inf

        while right < len(nums):
            if nums[right]-nums[left] < minimum:
                minimum = nums[right]-nums[left]
            right += 1
            left += 1
        return minimum
