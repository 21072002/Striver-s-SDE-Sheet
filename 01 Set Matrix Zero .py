'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        firstRowZero = False
        firstColZero = False

        # Step 1: Check if the first row and first column need to be zeroed initially
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
                break

        # Step 2: Mark rows and columns to be zeroed based on the elements
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the corresponding row
                    matrix[0][j] = 0  # Mark the corresponding column

        # Step 3: Update the matrix based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out the first row if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 5: Zero out the first column if needed
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0



solution = Solution()

# Test case 1
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix1)
print(matrix1)  # Expected output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# Test case 2
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix2)
print(matrix2)  # Expected output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

# Test case 3
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.setZeroes(matrix3)
print(matrix3)  # Expected output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] (no zeroes)

# Test case 4
matrix4 = [[1, 0, 3], [4, 5, 6], [7, 0, 9]]
solution.setZeroes(matrix4)
print(matrix4)  # Expected output: [[0, 0, 0], [4, 0, 6], [0, 0, 0]]

# Test case 5
matrix5 = [[1, 0]]
solution.setZeroes(matrix5)
print(matrix5)  # Expected output: [[0, 0]]
