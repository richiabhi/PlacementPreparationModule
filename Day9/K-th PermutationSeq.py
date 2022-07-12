import math


class Solution:
    def getPermutation(self, n: int, k: int):
        fact = math.factorial(n - 1)
        numbers, ans = list(range(1, n + 1)), ''
        k -= 1
        while True:
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)
            if len(numbers) == 0:
                break
            k %= fact
            fact //= len(numbers)
        return ans
