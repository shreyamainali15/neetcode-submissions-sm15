class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:

                mid = (left + right) // 2

                if row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1
                else:
                    return True

        return False
        