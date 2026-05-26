class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:

            mid = len(nums)//2

            left  = self.mergeSort(nums[:mid])
            right = self.mergeSort(nums[mid:])

            return self.merge(left,right)
        
        else:
            return nums


    def merge(self, left: List[int], right: List[int]) -> List[int]:
        temp = []
        index1 = 0
        index2 = 0
        while index1 < len(left) and index2 < len(right):
            if left[index1] <= right[index2]:
                temp.append(left[index1])
                index1 += 1
            else:
                temp.append(right[index2])
                index2 += 1
        
        while index1 < len(left):
            temp.append(left[index1])
            index1+=1

        while index2 < len(right):
            temp.append(right[index2])
            index2+=1

        return temp



