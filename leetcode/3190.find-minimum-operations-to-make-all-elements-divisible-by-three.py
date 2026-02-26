#
# @lc app=leetcode id=3190 lang=python3
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
#
# algorithms
# Easy (90.91%)
# Likes:    509
# Dislikes: 34
# Total Accepted:    264.1K
# Total Submissions: 290.5K
# Testcase Example:  '[1,2,3,4]'
#
# You are given an integer array nums. In one operation, you can add or
# subtract 1 from any element of nums.
#
# Return the minimum number of operations to make all elements of nums
# divisible by 3.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
#
# Output: 3
#
# Explanation:
#
# All array elements can be made divisible by 3 using 3 operations:
#
#
# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
#
#
#
# Example 2:
#
#
# Input: nums = [3,6,9]
#
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
#
#
#

# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # To make an element divisible by 3, we need to either add 1 or subtract 1 from it if it's not already divisible by 3. Therefore, the number of operations needed for each element is 1 if it's not divisible by 3, and 0 if it is. We can simply sum up the number of elements that are not divisible by 3 to get the total number of operations needed.
        # Time complexity: O(n), where n is the length of the input array nums.
        # Space complexity: O(1), since we are using a constant amount of extra space.

        # Count and return the total number of elements that are not divisible by 3
        return sum(n % 3 != 0 for n in nums)


# @lc code=end
