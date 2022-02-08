class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_v = 0
        val = 0
        c = 0
        set_nums =list(set(nums))
        for num in set_nums:
            c = nums.count(num)
            if c > max_v:
                max_v=c
                val=num
        if max_v>len(nums)//2:
            return val