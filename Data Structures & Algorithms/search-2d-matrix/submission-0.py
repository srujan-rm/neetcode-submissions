class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # ascending or equal order.
        # you can flatten the matrix to an array
        # how do we use binary search to find target 
        m, n = len(matrix), len(matrix[0])
        lp_i, lp_j, rp_i, rp_j = 0, 0, m - 1, n - 1
        lp = lp_j + lp_i * n
        rp = rp_j + rp_i * n 
        while (lp <= rp):
            mid = lp + ((rp - lp) // 2)
            mid_i, mid_j = mid // n, mid % n 
            if (matrix[mid_i][mid_j] == target):
                return True
            elif (matrix[mid_i][mid_j] < target):
                lp = mid + 1
            else:
                rp = mid - 1 
        return False 