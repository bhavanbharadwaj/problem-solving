class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_pattern(nums):
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr = max(prev2+nums[i], prev1)
                prev2 = prev1
                prev1 = curr
            
            return prev1
        
        if len(nums) <= 2:
            if len(nums) == 1:
                return nums[0]
            return max(nums[0], nums[1])
        
        return max(rob_pattern(nums[:-1]), rob_pattern(nums[1:]))