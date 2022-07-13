class Solution:
    def findPath(self, m, n):
        def ratInMaze(i, j, m, n, visited, moves=""):
            if i == n-1 and j == n-1:
                ans.append(moves)
                return
            #Downward
            if i+1 < n and not(visited[i+1][j]) and m[i+1][j] == 1:
                visited[i][j] = True
                ratInMaze(i+1, j, m, n, visited, moves+'D')
                visited[i][j] = False

            #Leftward
            if j-1 >= 0 and not(visited[i][j-1]) and m[i][j-1] == 1:
                visited[i][j] = True
                ratInMaze(i, j-1, m, n, visited, moves+'L')
                visited[i][j] = False

            #Rightward
            if j+1 < n and not(visited[i][j+1]) and m[i][j+1] == 1:
                visited[i][j] = True
                ratInMaze(i, j+1, m, n, visited, moves+"R")
                visited[i][j] = False
            #Upward
            if i-1 >= 0 and not(visited[i-1][j]) and m[i-1][j] == 1:
                visited[i][j] = True
                ratInMaze(i-1, j, m, n, visited, moves+"U")
                visited[i][j] = False

        ans = []
        visited = [[False for _ in range(n)]for _ in range(n)]
        if m[0][0] == 1:
            ratInMaze(0, 0, m, n, visited)
        return ans
