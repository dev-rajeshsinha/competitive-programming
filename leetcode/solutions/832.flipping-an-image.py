#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#
# https://leetcode.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (83.57%)
# Likes:    3708
# Dislikes: 260
# Total Accepted:    549.4K
# Total Submissions: 657.2K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# Given an n x n binary matrix image, flip the image horizontally, then invert
# it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is
# reversed.
#
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
#
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced
# by 0.
#
#
# For example, inverting [0,1,1] results in [1,0,0].
#
#
#
# Example 1:
#
#
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#
#
# Example 2:
#
#
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row:
# [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#
#
# Constraints:
#
#
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # # The approach is to use two pointers, one at the beginning and one at the end of each row. We will swap the values at these two pointers and then move the pointers towards the center of the row. We will also invert the values at these pointers by using the XOR operator with 1 (i.e., value ^ 1 will flip 0 to 1 and 1 to 0) before swapping them.
        # # Time complexity: O(n^2) since we need to iterate through each element of the image once.
        # # Space complexity: O(1) since we are modifying the image in place and not using any additional data structures.

        # # Iterate through each row in the image
        # for row in image:
        #     # Start two pointers at the beginning and end of the row
        #     first_pointer = 0
        #     last_pointer = len(row) - 1

        #     # Continue swapping and inverting until the pointers meet or cross
        #     while first_pointer <= last_pointer:
        #         # Swap and invert the values at the two pointers
        #         row[first_pointer], row[last_pointer] = (
        #             row[last_pointer] ^ 1,
        #             row[first_pointer] ^ 1,
        #         )

        #         # Move the pointers towards the center
        #         first_pointer += 1
        #         last_pointer -= 1

        # # Return the modified image
        # return image

        # We can also achieve the same result using a more concise approach by using list comprehensions. We can reverse each row and then invert the bits in a single step.
        # Time complexity: O(n^2) since we need to iterate through each element of the image once.
        # Space complexity: O(n^2) since we are creating a new image with the flipped and inverted values.

        # Flip and invert the image using list comprehensions and bitwise XOR to invert the bits in a single step while reversing the rows. Finally, return the modified image.
        return [[bit ^ 1 for bit in reversed(row)] for row in image]


# @lc code=end
