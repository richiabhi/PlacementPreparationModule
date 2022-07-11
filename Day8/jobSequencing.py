class Solution:
    def JobScheduling(self, Jobs, n):
        Jobs = sorted(Jobs, key=lambda Jobs: Jobs.profit, reverse=True)
        sortedDeadline = sorted(
            Jobs, key=lambda Jobs: Jobs.deadline, reverse=True)
        maxDeadline = sortedDeadline[0].deadline
        slots = [0]*(maxDeadline+1)
        taken = 0
        a = []
        profit = 0
        for job in Jobs:
            if job.deadline <= maxDeadline and slots[job.deadline] != 1:
                slots[job.deadline] = 1
                profit += job.profit
                taken += 1
            else:
                for i in range(job.deadline, 0, -1):
                    if slots[i] != 1:
                        slots[i] = 1
                        profit += job.profit
                        taken += 1
                        break
        return taken, profit
