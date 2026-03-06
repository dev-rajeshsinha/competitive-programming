#
# @lc app=leetcode id=2859 lang=python3
#
# [2859] Sum of Values at Indices With K Set Bits
#
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/
#
# algorithms
# Easy (86.09%)
# Likes:    318
# Dislikes: 50
# Total Accepted:    95.7K
# Total Submissions: 111.2K
# Testcase Example:  '[5,10,1,5,2]\n1'
#
# You are given a 0-indexed integer array nums and an integer k.
#
# Return an integer that denotes the sum of elements in nums whose
# corresponding indices have exactly k set bits in their binary
# representation.
#
# The set bits in an integer are the 1's present when it is written in
# binary.
#
#
# For example, the binary representation of 21 is 10101, which has 3 set
# bits.
#
#
#
# Example 1:
#
#
# Input: nums = [5,10,1,5,2], k = 1
# Output: 13
# Explanation: The binary representation of the indices are:
# 0 = 0002
# 1 = 0012
# 2 = 0102
# 3 = 0112
# 4 = 1002
# Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
# Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
#
# Example 2:
#
#
# Input: nums = [4,3,2,1], k = 2
# Output: 1
# Explanation: The binary representation of the indices are:
# 0 = 002
# 1 = 012
# 2 = 102
# 3 = 112
# Only index 3 has k = 2 set bits in its binary representation.
# Hence, the answer is nums[3] = 1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^5
# 0 <= k <= 10
#
#
#

# @lc code=start
from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # The approach is straightforward: we iterate through the indices of the nums array,
        # check if the number of set bits in the index is equal to k, and if so, we add the corresponding value from nums to our sum.
        # The bit_count() method is used to count the number of set bits in the binary representation of the index.
        # Time complexity: O(n), where n is the length of the nums array, since we need to check each index once.
        # Space complexity: O(1), as we are using a constant amount of extra space to store the sum.

        # Using a generator expression to iterate through the indices and values of nums, we check if the bit count of the index is equal to k. If it is, we include the corresponding value in the sum. Finally, we return the total sum.
        return sum(value for index, value in enumerate(nums) if index.bit_count() == k)


# @lc code=end
