class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci Binet's Formula

        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)