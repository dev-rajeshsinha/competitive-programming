#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (82.75%)
# Likes:    5476
# Dislikes: 199
# Total Accepted:    255.2K
# Total Submissions: 308.3K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# You are given an m x n integer array grid where grid[i][j] could be:
#
#
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
#
#
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
#
# Example 2:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#
# Example 3:
#
#
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly
# once.
# Note that the starting and ending square can be anywhere in the grid.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# 1 <= m * n <= 20
# -1 <= grid[i][j] <= 2
# There is exactly one starting cell and one ending cell.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # This approach uses Depth-First Search (DFS) with Backtracking to explore all possible paths from the starting square to the ending square while ensuring that every empty square is visited exactly once. The algorithm can be broken down into the following steps:
        # Step 1: Grid Initialization
        # Iterate through the grid once to locate the starting coordinates, ending coordinates, and to count the total number of empty squares (total_movable_blocks) that must be visited.
        # Step 2: Backtracking (DFS) Exploration
        # - Base Case Validation: If the current cell is the ending square, we check if our (steps_taken - 1) equals the total_movable_blocks. If they match, it means we successfully stepped on every empty square exactly once before reaching the end.
        # - State Mutation (Marking Visited): Before exploring neighbors, we temporarily mark the current square as visited (change to -1) to prevent the path from looping back onto itself.
        # - Recursive Branching: We attempt to move Up, Down, Left, and Right into any square that is not a grid boundary and not marked as visited (-1).
        # - State Restoration (Backtracking): Once all paths from the current square are fully explored, we "backtrack" by restoring the square back to its original value. This allows the square to be explored again via completely different path combinations.
        # Time Complexity: O(3^(N*M)) where N and M are the dimensions of the grid. This is because in the worst case, we may explore all possible paths through the grid, which can be exponential in nature.
        # Space Complexity: O(N*M) due to the recursive call stack in the worst case when the path explores all cells in the grid.

        # Store dimensions of the grid for easy access
        n = len(grid)
        m = len(grid[0])

        # Initialize variables to store the starting position, ending position, total number of empty squares, and total possible paths
        starting_pos = (0, 0)
        ending_pos = (0, 0)
        total_movable_blocks = 0
        total_possible_path = 0

        # Iterate through the grid to find the starting and ending positions, and count the total number of empty squares
        for row in range(0, n):
            for col in range(0, m):
                if grid[row][col] == 1:
                    starting_pos = (row, col)
                elif grid[row][col] == 2:
                    ending_pos = (row, col)
                elif grid[row][col] == 0:
                    total_movable_blocks += 1

        # Define the backtracking function to explore all paths from the current position
        def backtrack(current_row, current_col, steps_taken):
            # Use nonlocal to modify the variables defined in the outer scope
            nonlocal n, m, ending_pos, total_movable_blocks, total_possible_path

            # Base case: If the current position is the ending position, check if we have stepped on all empty squares
            if current_row == ending_pos[0] and current_col == ending_pos[1]:
                # If steps_taken - 1 equals total_movable_blocks, it means we have successfully visited all empty squares exactly once before reaching the end (we subtract 1 because the ending square is not counted as a movable block), and we can increment the total_possible_path count by 1.
                total_possible_path += (
                    1 if steps_taken - 1 == total_movable_blocks else 0
                )
            # If the current position is not the ending position, we need to explore further by marking the current square as visited and recursively calling backtrack for all valid neighboring squares (up, down, left, right).
            else:
                # Store the current grid value before marking it as visited, so we can restore it later during backtracking
                current_grid_value = grid[current_row][current_col]

                # Mark the current square as visited by setting it to -1
                grid[current_row][current_col] = -1

                # Explore all four possible directions (up, down, left, right) if they are within the grid boundaries and not marked as visited (-1) and recursively call backtrack for each valid move, incrementing the steps_taken by 1 for each move.
                if current_row > 0 and grid[current_row - 1][current_col] != -1:
                    backtrack(current_row - 1, current_col, steps_taken + 1)
                if current_row < n - 1 and grid[current_row + 1][current_col] != -1:
                    backtrack(current_row + 1, current_col, steps_taken + 1)
                if current_col > 0 and grid[current_row][current_col - 1] != -1:
                    backtrack(current_row, current_col - 1, steps_taken + 1)
                if current_col < m - 1 and grid[current_row][current_col + 1] != -1:
                    backtrack(current_row, current_col + 1, steps_taken + 1)

                # Restore the current square's original value after exploring all paths from it (backtracking step) so that it can be used again in different path combinations.
                grid[current_row][current_col] = current_grid_value

        # Start the backtracking process from the starting position with an initial step count of 0.
        backtrack(starting_pos[0], starting_pos[1], 0)

        # After exploring all possible paths, return the total count of valid paths from the starting square to the ending square that visit every empty square exactly once.
        return total_possible_path


# @lc code=end
