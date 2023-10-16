'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []  # Initialize a list to store the triangle rows.

        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize a row with '1's of length (i + 1).

            # Calculate the values for the inner elements of the row.
            for j in range(1, i):
                # Each element (except the first and last) is the sum of the two elements above it.
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)  # Add the current row to the triangle.

        return triangle  # Return the generated Pascal's Triangle.

# Test cases
solution = Solution()

# Test case 1
numRows1 = 5
print(f"Pascal's Triangle for numRows = {numRows1}:")
print(solution.generate(numRows1))
# Expected output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Test case 2
numRows2 = 1
print(f"Pascal's Triangle for numRows = {numRows2}:")
print(solution.generate(numRows2))
# Expected output: [[1]]


