class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        t, b = 0, rows - 1
       
        while t <= b:
            row = t + (b - t) // 2
            if target < matrix[row][0]:
                b = row - 1
            elif target > matrix[row][-1]:
                t = row + 1
            else:
                final_row = row
                break
        
        if not (t <= b):
            return False

        left, right = 0, cols - 1
        
        while (left <= right):
            mid = left + (right - left) // 2

            if (matrix[final_row][mid] < target):
                left = mid + 1
            elif (matrix[final_row][mid] > target):
                right = mid - 1
            else:
                return True
        
        
        return False




