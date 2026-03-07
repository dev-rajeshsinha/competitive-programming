#
# @lc app=leetcode id=3688 lang=python3
#
# [3688] Bitwise OR of Even Numbers in an Array
#
# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/description/
#
# algorithms
# Easy (84.74%)
# Likes:    35
# Dislikes: 4
# Total Accepted:    70.9K
# Total Submissions: 83.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# You are given an integer array nums.
#
# Return the bitwise OR of all even numbers in the array.
#
# If there are no even numbers in nums, return 0.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5,6]
#
# Output: 6
#
# Explanation:
#
# The even numbers are 2, 4, and 6. Their bitwise OR equals 6.
#
#
# Example 2:
#
#
# Input: nums = [7,9,11]
#
# Output: 0
#
# Explanation:
#
# There are no even numbers, so the result is 0.
#
#
# Example 3:
#
#
# Input: nums = [1,8,16]
#
# Output: 24
#
# Explanation:
#
# The even numbers are 8 and 16. Their bitwise OR equals 24.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#

# @lc code=start
from typing import List
from functools import reduce
from operator import or_


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        # The approach is to use the reduce function from the functools module to apply the bitwise OR operation to all even numbers in the array. We can use a generator expression to filter out the even numbers and apply the OR operation starting with an initial value of 0.
        # Time complexity: O(n), where n is the length of the input array nums, since we need to iterate through the array once to filter out the even numbers and apply the OR operation.
        # Space complexity: O(1), since we are using a constant amount of space to store the intermediate result of the OR operation.

        # Return the bitwise OR of all even numbers in the array, or 0 if there are no even numbers.
        return reduce(or_, (num for num in nums if num & 1 == 0), 0)


# @lc code=end
