class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        con=len(nums)-nums.count(val)
        for i in range(len(nums)-con):
                nums.remove(val)

        print(nums)

        return con