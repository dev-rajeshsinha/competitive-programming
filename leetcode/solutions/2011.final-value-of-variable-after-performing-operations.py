#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
#
# algorithms
# Easy (90.56%)
# Likes:    2018
# Dislikes: 216
# Total Accepted:    642.8K
# Total Submissions: 709.8K
# Testcase Example:  '["--X","X++","X++"]'
#
# There is a programming language with only four operations and one variable
# X:
#
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
#
#
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return
# the final value of X after performing all the operations.
#
#
# Example 1:
#
#
# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.
#
#
# Example 2:
#
#
# Input: operations = ["++X","++X","X++"]
# Output: 3
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# ++X: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# X++: X is incremented by 1, X = 2 + 1 = 3.
#
#
# Example 3:
#
#
# Input: operations = ["X++","++X","--X","X--"]
# Output: 0
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# X++: X is incremented by 1, X = 0 + 1 = 1.
# ++X: X is incremented by 1, X = 1 + 1 = 2.
# --X: X is decremented by 1, X = 2 - 1 = 1.
# X--: X is decremented by 1, X = 1 - 1 = 0.
#
#
#
# Constraints:
#
#
# 1 <= operations.length <= 100
# operations[i] will be either "++X", "X++", "--X", or "X--".
#
#
#

# @lc code=start
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # We can iterate through the list of operations and check the second character of each operation to determine whether to increment or decrement the variable X. If the second character is '+', we increment X by 1; if it is '-', we decrement X by 1. We can use a generator expression inside the sum function to calculate the final value of X after performing all operations.
        # Time complexity: O(n), where n is the number of operations.
        # Space complexity: O(1), as we are using a constant amount of space to store the final value of X.

        # Iterate through the list of operations and calculate the final value of X
        return sum(1 if op[1] == "+" else -1 for op in operations)


# @lc code=end
