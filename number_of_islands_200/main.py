from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Idea is to do a have a check matrix and perform
        a BFS on the original matrix and recurse on it
        """
        count = 0
        check_matrix = [
            [False for _ in range(len(grid[0]))] for _ in range(len(grid))
            ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                """
                Perform search here now if
                """
                if (grid[i][j] == '1' and check_matrix[i][j] is False):
                    self.search(grid, check_matrix, i, j)
                    count += 1
        return count

    def search(self, grid, check_matrix, i, j):
        qu = deque([(i, j)])
        while qu:
            i, j = qu.popleft()
            if (
                0 <= i < len(grid)
                and 0 <= j < len(grid[0])
                and grid[i][j] == "1"
                and check_matrix[i][j] is False
            ):
                check_matrix[i][j] = True
                qu.extend([(i+1, j), (i, j+1), (i-1, j), (i, j-1)])


solution = Solution()
return_val = solution.numIslands(
    grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "1", "1"]
        ]
)
print(f"Number of islands -> {return_val}")
