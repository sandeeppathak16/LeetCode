class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        if len(nums) <= 2:
            return max(nums[0:2])

        dp[0] = nums[0]
        dp[1] = max(nums[0:2])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return max(dp[-1], dp[-2])
        