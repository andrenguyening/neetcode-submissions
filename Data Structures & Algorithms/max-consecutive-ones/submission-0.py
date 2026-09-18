class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                print(cnt)
            else:
                max_con = max(max_con, cnt)
                cnt = 0
        max_con = max(max_con, cnt)
        return max_con

