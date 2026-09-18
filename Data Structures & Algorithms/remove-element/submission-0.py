class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = len(nums)
        while i < k:
            if nums[i] == val:
                k -= 1
                nums[i] = nums[k]
            else:
                i += 1
        return k