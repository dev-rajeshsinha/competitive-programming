#
# @lc app=leetcode id=3701 lang=python3
#
# [3701] Compute Alternating Sum
#
# https://leetcode.com/problems/compute-alternating-sum/description/
#
# algorithms
# Easy (89.69%)
# Likes:    63
# Dislikes: 2
# Total Accepted:    67.3K
# Total Submissions: 75.1K
# Testcase Example:  '[1,3,5,7]'
#
# You are given an integer array nums.
#
# The alternating sum of nums is the value obtained by adding elements at even
# indices and subtracting elements at odd indices. That is, nums[0] - nums[1] +
# nums[2] - nums[3]...
#
# Return an integer denoting the alternating sum of nums.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,7]
#
# Output: -4
#
# Explanation:
#
#
# Elements at even indices are nums[0] = 1 and nums[2] = 5 because 0 and 2 are
# even numbers.
# Elements at odd indices are nums[1] = 3 and nums[3] = 7 because 1 and 3 are
# odd numbers.
# The alternating sum is nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7
# = -4.
#
#
#
# Example 2:
#
#
# Input: nums = [100]
#
# Output: 100
#
# Explanation:
#
#
# The only element at even indices is nums[0] = 100 because 0 is an even
# number.
# There are no elements on odd indices.
# The alternating sum is nums[0] = 100.
#
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


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        # The approach is to iterate through the input list and calculate the alternating sum by adding elements at even indices and subtracting elements at odd indices. We can achieve this by using a generator expression that checks the index of each element and adds or subtracts it accordingly.
        # Time complexity: O(n), where n is the length of the input list. We iterate through the list once to calculate the alternating sum.
        # Space complexity: O(1), as we are using a constant amount of space to store the alternating sum.

        # Calculate the alternating sum using a generator expression that checks the index of each element, then adds or subtracts it accordingly based on whether the index is even or odd, and finally returns the total sum.
        return sum(
            value if index & 1 == 0 else -value for index, value in enumerate(nums)
        )


# @lc code=end
