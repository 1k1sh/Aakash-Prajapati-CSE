import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=[[0]*n]*m
        for i in range(m):
            a[i][0]=1
        for j in range(n):
            a[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                a[i][j]=a[i-1][j]+a[i][j-1]
        return a[m-1][n-1]