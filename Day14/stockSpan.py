from collections import deque


class StockSpanner:

    def __init__(self):
        self.stack = deque()
        self.count = -1

    def next(self, price: int) -> int:
        self.count += 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        ans = 0
        if self.stack:
            ans = self.count - self.stack[-1][1]
        else:
            ans = self.count + 1
        self.stack.append([price, self.count])
        return ans
