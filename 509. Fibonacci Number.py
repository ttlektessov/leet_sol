class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        fibb = 0
        a, b = 0, 1
        for i in range(n-1):
            fibb = a + b
            a = b
            b = fibb
        return fibb
