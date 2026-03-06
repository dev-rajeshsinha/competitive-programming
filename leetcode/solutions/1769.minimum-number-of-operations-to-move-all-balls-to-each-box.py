#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
#
# algorithms
# Medium (90.13%)
# Likes:    3118
# Dislikes: 139
# Total Accepted:    334.1K
# Total Submissions: 370.7K
# Testcase Example:  '"110"'
#
# You have n boxes. You are given a binary string boxes of length n, where
# boxes[i] is '0' if the i^th box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box. Box i
# is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may
# be more than one ball in some boxes.
#
# Return an array answer of size n, where answer[i] is the minimum number of
# operations needed to move all the balls to the i^th box.
#
# Each answer[i] is calculated considering the initial state of the boxes.
#
#
# Example 1:
#
#
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first
# box in one operation.
# 2) Second box: you will have to move one ball from the first box to the
# second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third
# box in two operations, and move one ball from the second box to the third box
# in one operation.
#
#
# Example 2:
#
#
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
#
#
# Constraints:
#
#
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # The idea is to calculate the number of movement needed to move all the balls to the current box from left and right side separately for each box. In order to calculate the number of movement needed for each box, we can use two loops. In the first loop, we can calculate the number of movement needed to move all the balls to the current box from left side for each box. In the second loop, we can calculate the number of movement needed to move all the balls to the current box from right side for each box. Finally, we can add the number of movement needed to move all the balls to the current box from left and right side for each box and return the result.
        # Time complexity: O(n) where n is the length of the input string
        # Space complexity: O(n) for the result array

        # Initialize variables to keep track of the number of balls found till the last box and movements needed to move all the balls to the last box
        number_of_ball_till_last_box = 0
        number_of_movement_till_last_box = 0

        # Initialize the result array to store the minimum number of operations needed to move all the balls to the current box for each box
        result = [0] * len(boxes)

        # Calculate the number of movement needed to move all the balls to the current box from left side for each box
        for i in range(len(boxes)):
            # For each box, the number of movement needed to move all the balls to the current box from left side is equal to the number of balls found till the last box plus the number of movements needed to move all the balls to the last box. We can update the number of movements needed to move all the balls to the last box by adding the number of balls found till the last box. Finally, if the current box contains a ball, we can update the number of balls found till the last box by adding 1.
            result[i] += number_of_ball_till_last_box + number_of_movement_till_last_box
            number_of_movement_till_last_box += number_of_ball_till_last_box
            if boxes[i] == "1":
                number_of_ball_till_last_box += 1

        # Reset the variables to keep track of the number of balls found till the last box and movements needed to move all the balls to the last box for the second loop
        number_of_ball_till_last_box = 0
        number_of_movement_till_last_box = 0

        # Calculate the number of movement needed to move all the balls to the current box from right side for each box
        for i in range(len(boxes) - 1, -1, -1):
            # For each box, the number of movement needed to move all the balls to the current box from right side is equal to the number of balls found till the last box plus the number of movements needed to move all the balls to the last box. We can update the number of movements needed to move all the balls to the last box by adding the number of balls found till the last box. Finally, if the current box contains a ball, we can update the number of balls found till the last box by adding 1.
            result[i] += number_of_ball_till_last_box + number_of_movement_till_last_box
            number_of_movement_till_last_box += number_of_ball_till_last_box
            if boxes[i] == "1":
                number_of_ball_till_last_box += 1

        # Finally, we can return the result array which contains the minimum number of operations needed to move all the balls to the current box for each box.
        return result


# @lc code=end
