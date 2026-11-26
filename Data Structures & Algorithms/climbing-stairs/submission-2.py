class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2
        answer = 0

        for num in range(3, n+1):
            answer = prev2 + prev1
            prev2 = prev1
            prev1 = answer
        
        return answer
        