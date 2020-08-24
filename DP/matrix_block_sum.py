"""
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all
elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
"""

def createDPMatrix(mat):
    # DP matrix containing an extra row and col at beginning
    DP = [[0 for i in range(len(mat[0])+1)] for j in range(len(mat)+1)]
    
    for i in range(1,len(mat)+1):
        for j in range(1,len(mat[0])+1):
            DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + mat[i-1][j-1]
    return DP

def matrixBlockSum(mat, K):
    dp = createDPMatrix(mat)
    # Height and breadth
    h = len(mat)
    b = len(mat[0])
    
    result = [[0 for j in range(b)] for i in range(h)]
    for i in range(h):
        for j in range(b):
            # Vertices of the rectangle to find the sum 
            x1 = max(0, i-K)
            y1 = max(0, j-K)
            x2 = min(h-1, i+K)+1
            y2 = min(b-1, j+K)+1
            
            result[i][j] = dp[x2][y2] - dp[x1][y2] - dp[x2][y1] + dp[x1][y1]
    return result

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
K = 2
print(matrixBlockSum(mat, K))
# Output: [[54, 78, 78, 63], [54, 78, 78, 63], [54, 78, 78, 63]]