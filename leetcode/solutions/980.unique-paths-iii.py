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
from functools import cache


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # # This approach uses Depth-First Search (DFS) with Backtracking to explore all possible paths from the starting square to the ending square while ensuring that every empty square is visited exactly once. The algorithm can be broken down into the following steps:
        # # Step 1: Grid Initialization
        # # Iterate through the grid once to locate the starting coordinates, ending coordinates, and to count the total number of empty squares (total_movable_blocks) that must be visited.
        # # Step 2: Backtracking (DFS) Exploration
        # # - Base Case Validation: If the current cell is the ending square, we check if our (steps_taken - 1) equals the total_movable_blocks. If they match, it means we successfully stepped on every empty square exactly once before reaching the end.
        # # - State Mutation (Marking Visited): Before exploring neighbors, we temporarily mark the current square as visited (change to -1) to prevent the path from looping back onto itself.
        # # - Recursive Branching: We attempt to move Up, Down, Left, and Right into any square that is not a grid boundary and not marked as visited (-1).
        # # - State Restoration (Backtracking): Once all paths from the current square are fully explored, we "backtrack" by restoring the square back to its original value. This allows the square to be explored again via completely different path combinations.
        # # Time Complexity: O(3^(N*M)) where N and M are the dimensions of the grid. This is because in the worst case, we may explore all possible paths through the grid, which can be exponential in nature.
        # # Space Complexity: O(N*M) due to the recursive call stack in the worst case when the path explores all cells in the grid.

        # # Store dimensions of the grid for easy access
        # n = len(grid)
        # m = len(grid[0])

        # # Initialize variables to store the starting position, ending position, total number of empty squares, and total possible paths
        # starting_pos = (0, 0)
        # ending_pos = (0, 0)
        # total_movable_blocks = 0
        # total_possible_path = 0

        # # Iterate through the grid to find the starting and ending positions, and count the total number of empty squares
        # for row in range(0, n):
        #     for col in range(0, m):
        #         if grid[row][col] == 1:
        #             starting_pos = (row, col)
        #         elif grid[row][col] == 2:
        #             ending_pos = (row, col)
        #         elif grid[row][col] == 0:
        #             total_movable_blocks += 1

        # # Define the backtracking function to explore all paths from the current position
        # def backtrack(current_row, current_col, steps_taken):
        #     # Use nonlocal to modify the variables defined in the outer scope
        #     nonlocal n, m, ending_pos, total_movable_blocks, total_possible_path

        #     # Base case: If the current position is the ending position, check if we have stepped on all empty squares
        #     if current_row == ending_pos[0] and current_col == ending_pos[1]:
        #         # If steps_taken - 1 equals total_movable_blocks, it means we have successfully visited all empty squares exactly once before reaching the end (we subtract 1 because the ending square is not counted as a movable block), and we can increment the total_possible_path count by 1.
        #         total_possible_path += (
        #             1 if steps_taken - 1 == total_movable_blocks else 0
        #         )
        #     # If the current position is not the ending position, we need to explore further by marking the current square as visited and recursively calling backtrack for all valid neighboring squares (up, down, left, right).
        #     else:
        #         # Store the current grid value before marking it as visited, so we can restore it later during backtracking
        #         current_grid_value = grid[current_row][current_col]

        #         # Mark the current square as visited by setting it to -1
        #         grid[current_row][current_col] = -1

        #         # Explore all four possible directions (up, down, left, right) if they are within the grid boundaries and not marked as visited (-1) and recursively call backtrack for each valid move, incrementing the steps_taken by 1 for each move.
        #         if current_row > 0 and grid[current_row - 1][current_col] != -1:
        #             backtrack(current_row - 1, current_col, steps_taken + 1)
        #         if current_row < n - 1 and grid[current_row + 1][current_col] != -1:
        #             backtrack(current_row + 1, current_col, steps_taken + 1)
        #         if current_col > 0 and grid[current_row][current_col - 1] != -1:
        #             backtrack(current_row, current_col - 1, steps_taken + 1)
        #         if current_col < m - 1 and grid[current_row][current_col + 1] != -1:
        #             backtrack(current_row, current_col + 1, steps_taken + 1)

        #         # Restore the current square's original value after exploring all paths from it (backtracking step) so that it can be used again in different path combinations.
        #         grid[current_row][current_col] = current_grid_value

        # # Start the backtracking process from the starting position with an initial step count of 0.
        # backtrack(starting_pos[0], starting_pos[1], 0)

        # # After exploring all possible paths, return the total count of valid paths from the starting square to the ending square that visit every empty square exactly once.
        # return total_possible_path

        # There is an alternate approach to solve this problem using Dynamic Programming with Bitmasking. This is a Hamiltonian Path problem on a grid. The idea is to use a bitmask to represent the set of visited cells and a recursive function with memoization to count the number of valid paths. Here's how we can implement this:

        # Algorithm Breakdown:
        # Grid Flattening & Target Mask:
        # Instead of mutating the 2D grid, we assign every cell a unique 1D index using the formula: (row * total_columns + column).
        # We create a `complete_traversal_mask` where the bit at each valid cell's index is set to 1. Obstacles (-1) are left as 0.

        # State Representation (The Bitmask):
        # As we traverse the grid, we pass an integer (`current_mask`) down the recursive call stack. If we visit a cell, we flip its specific bit to 1. This immutable integer completely replaces the need to modify the grid array and clean it up afterward.

        # Memoization (@cache):
        # Because paths can overlap on certain graph configurations, Python's @cache decorator memorizes the result of (current_row, current_col, current_mask). If we ever reach the exact same cell with the exact same visitation history, it instantly returns the saved path count in O(1) time.
        # Time Complexity: O(R * C * 2^(R*C)) where R is the number of rows and C is the number of columns in the grid. This is because we potentially explore every cell with every possible combination of visited cells (represented by the bitmask).
        # Space Complexity: O(R * C * 2^(R*C)) due to the memoization cache storing results for each unique state of (current_row, current_column, current_mask).

        # Calculate total rows and columns in the grid for easy access
        total_rows = len(grid)
        total_columns = len(grid[0])

        # Initialize variables to store the starting and ending indices, and the complete traversal mask
        starting_index_row = starting_index_column = 0
        ending_index_row = ending_index_column = 0
        complete_traversal_mask = 0

        # Iterate through the grid
        for r in range(0, total_rows):
            for c in range(0, total_columns):
                # Check if the current cell is the starting square (1)
                if grid[r][c] == 1:
                    # If it is, store its row and column indices as the starting position
                    starting_index_row, starting_index_column = r, c
                # Check if the current cell is the ending square (2)
                elif grid[r][c] == 2:
                    # If it is, store its row and column indices as the ending position
                    ending_index_row, ending_index_column = r, c

                # Check if the current cell is not an obstacle (-1) (it can be either 0, 1, or 2)
                if grid[r][c] != -1:
                    # If it is a valid cell, calculate its flattened index and set the corresponding bit in the complete_traversal_mask to 1 to indicate that this cell needs to be visited in the path from start to end.
                    flattened_cell_index = r * total_columns + c
                    complete_traversal_mask |= 1 << flattened_cell_index

        @cache
        def dp(current_row, current_column, current_mask) -> int:
            # Check if the current position is the ending position. If it is, we need to check if the current_mask (which represents all visited cells) matches the complete_traversal_mask (which represents all cells that need to be visited). If they match, it means we have successfully visited every required cell exactly once before reaching the end, and we return 1 to count this valid path. If they do not match, it means this path does not satisfy the requirement of visiting all cells, and we return 0.
            if (
                current_row == ending_index_row
                and current_column == ending_index_column
            ):
                # Return 1 if the current_mask matches the complete_traversal_mask, indicating a valid path, otherwise return 0.
                return 1 if complete_traversal_mask == current_mask else 0
            # If the current position is not the ending position, we need to explore further by trying to move in all four possible directions (up, down, left, right) from the current cell.
            else:
                # Define the possible movements in terms of row and column changes for up, down, left, and right directions.
                possible_movements = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                # Initialize a variable to count the total possible movements from the current position that lead to valid paths to the ending square.
                total_possible_movements_from_current_position = 0

                # Iterate through each possible movement direction
                for movement in possible_movements:
                    # Calculate the next row and column indices based on the current position and the movement direction.
                    next_row, next_column = (
                        current_row + movement[0],
                        current_column + movement[1],
                    )

                    # Calculate the flattened index for the next position using the formula: (next_row * total_columns + next_column).
                    next_flattened_index = next_row * total_columns + next_column

                    # Check if the next position is within the grid boundaries, is a valid cell to visit (not an obstacle), and has not been visited yet in the current path (checked using the current_mask).
                    if (
                        0 <= next_row < total_rows
                        and 0 <= next_column < total_columns
                        and complete_traversal_mask & (1 << next_flattened_index) != 0
                        and current_mask & (1 << next_flattened_index) == 0
                    ):
                        # If the next position is valid, we make a recursive call to the dp function with the next position and an updated mask that includes the next cell as visited (using bitwise OR to set the bit corresponding to the next cell's index). We add the result of this recursive call to our total_possible_movements_from_current_position, which accumulates the count of valid paths from the current position to the ending square.
                        total_possible_movements_from_current_position += dp(
                            next_row,
                            next_column,
                            current_mask | (1 << next_flattened_index),
                        )

                # After exploring all possible movements from the current position, we return the total count of valid paths that can be taken from this position to reach the ending square while visiting all required cells exactly once.
                return total_possible_movements_from_current_position

        # Calculate the flattened index for the starting position and initialize the running mask with the starting position's bit set to 1, indicating that we have visited the starting cell at the beginning of our path.
        flattened_start_index = (
            starting_index_row * total_columns + starting_index_column
        )
        running_mask = 1 << flattened_start_index

        # Start the recursive dynamic programming function from the starting position with the initial mask indicating that the starting cell has been visited. The function will explore all possible paths and return the total count of valid paths from the starting square to the ending square that visit every empty square exactly once.
        return dp(starting_index_row, starting_index_column, running_mask)


# @lc code=end
