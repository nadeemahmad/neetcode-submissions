class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxCount = 0
        currentCount = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                currentCount += 1
                maxCount = max(currentCount, maxCount)
            else:
                currentCount = 0
        
        return maxCount


        