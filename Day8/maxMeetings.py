class Solution:
    def maximumMeetings(self, n, start, end):
        jobs = [(start[i], end[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        cnt = 0
        prev = 0
        for i in range(n):
            if prev < jobs[i][0]:
                cnt += 1
                prev = jobs[i][1]
        return cnt
