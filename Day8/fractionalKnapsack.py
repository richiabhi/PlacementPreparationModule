class Solution:
    def fractionalknapsack(self, W, Items, n):
        data = []
        for i in range(n):
            ratio = Items[i].value/Items[i].weight
            data.append((ratio, Items[i].value, Items[i].weight))
        data.sort(reverse=True)
        profit = 0
        for i in range(n):
            value, wt = data[i][1], data[i][2]
            if W > wt:
                W -= wt
                profit += value
            else:
                leftWt = W/wt
                profit, W = profit+leftWt*value, 0
                break
        return profit
