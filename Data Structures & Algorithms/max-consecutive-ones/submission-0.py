class Solution:
    def findMaxConsecutiveOnes(self,nums: List[int]) -> int:
        con = 0
        max = 0

        for num in nums:
            if num == 1:
                con += 1
            else:
                con = 0
            if con > max:
                max = con

        return max