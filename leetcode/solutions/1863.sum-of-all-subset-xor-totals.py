#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
#
# algorithms
# Easy (90.09%)
# Likes:    2677
# Dislikes: 354
# Total Accepted:    352.2K
# Total Submissions: 390.9K
# Testcase Example:  '[1,3]'
#
# The XOR total of an array is defined as the bitwise XOR of all its elements,
# or 0 if the array is empty.
#
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
#
#
# Given an array nums, return the sum of all XOR totals for every subset of
# nums.
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting
# some (possibly zero) elements of b.
#
#
# Example 1:
#
#
# Input: nums = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6
#
#
# Example 2:
#
#
# Input: nums = [5,1,6]
# Output: 28
# Explanation: The 8 subsets of [5,1,6] are:
# - The empty subset has an XOR total of 0.
# - [5] has an XOR total of 5.
# - [1] has an XOR total of 1.
# - [6] has an XOR total of 6.
# - [5,1] has an XOR total of 5 XOR 1 = 4.
# - [5,6] has an XOR total of 5 XOR 6 = 3.
# - [1,6] has an XOR total of 1 XOR 6 = 7.
# - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
# 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
#
#
# Example 3:
#
#
# Input: nums = [3,4,5,6,7,8]
# Output: 480
# Explanation: The sum of all XOR totals for every subset is 480.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 12
# 1 <= nums[i] <= 20
#
#
#


# @lc code=start
from typing import List


class Solution:
    # def build_subset_and_calculate_xor(
    #     self, original_list: List[int], current_index: int, current_xor_total: int
    # ) -> int:
    #     """
    #     Recursive helper function to build all subsets and calculate their XOR totals.

    #     Args:
    #     - original_list: The original list of integers.
    #     - current_index: The current index in the list being considered.
    #     - current_xor_total: The XOR total of the subset built so far.

    #     Returns:
    #     - The sum of XOR totals for all subsets starting from the current index.
    #     """

    #     # Base case: if we've considered all elements, return the current XOR total.
    #     if current_index == len(original_list):
    #         return current_xor_total

    #     # Choice 1: do not include current element
    #     exclude_current = self.build_subset_and_calculate_xor(
    #         original_list, current_index + 1, current_xor_total
    #     )

    #     # Choice 2: include current element
    #     include_current = self.build_subset_and_calculate_xor(
    #         original_list,
    #         current_index + 1,
    #         current_xor_total ^ original_list[current_index],
    #     )

    #     # Return the sum of both choices.
    #     return exclude_current + include_current

    def subsetXORSum(self, nums: List[int]) -> int:
        # # The first approach is to build all subsets and calculate the XOR total for each subset. We can do this using a recursive function that takes the original list, the current index, and the current XOR total as parameters. At each step, we have two choices: either we include the current element in our subset or we exclude it. We will recursively call the function for both choices and sum up the results to get the final answer. The base case is when the current index is equal to the length of the original list, at which point we return the current XOR total.
        # # Time complexity: O(2^n) where n is the length of the input list, since we are generating all subsets.
        # # Space complexity: O(n) for the recursion stack in the worst case.

        # # Call the recursive function starting with index 0 and XOR total 0 (considering the empty subset).
        # return self.build_subset_and_calculate_xor(nums, 0, 0)

        # A more optimized approach is to use bit manipulation to find the total XOR of all elements in the input list, where we will iterate through each element and calculate OR of all elements. Then we can left shift by (n-1) to get the total sum of XOR totals for all subsets, where n is the length of the input list. This works because each bit in the total XOR will contribute to the XOR total of exactly half of the subsets (since each element can either be included or excluded), and there are 2^(n-1) such subsets for each bit.
        # Time complexity: O(n) where n is the length of the input list, since we are iterating through the list once to calculate the total XOR.
        # Space complexity: O(1) since we are using a constant amount of space.

        # Initialize total_xor to 0 and calculate the OR of all elements in the input list.
        total_xor = 0

        # Iterate through each element in the input list.
        for num in nums:
            # Update total_xor by performing a bitwise OR with the current element.
            total_xor |= num

        # Left shift total_xor by (n-1) to get the total sum of XOR totals for all subsets and return the result.
        return total_xor << (len(nums) - 1)

        # Here is a brief explanation of the bit manipulation approach in more detail:
        # 1. We first calculate the total XOR of all elements in the input list using a bitwise OR operation. This gives us a number where each bit is set to 1 if at least one element in the list has that bit set to 1.
        # 2. Each bit in the total XOR will contribute to the XOR total of exactly half of the subsets, because for each element, we have two choices (include or exclude), and this creates a binary tree of subsets where each level corresponds to including or excluding an element.
        # 3. Since there are 2^n subsets in total, each bit will contribute to the XOR total of 2^(n-1) subsets (half of the total subsets).
        # 4. Therefore, we can simply left shift the total XOR by (n-1) to account for the contribution of each bit to the XOR totals of all subsets, giving us the final result. Other than left shifting, we could also multiply total_xor by 2^(n-1) to achieve the same result, since left shifting by k is equivalent to multiplying by 2^k.
        # This approach is much more efficient than generating all subsets and calculating their XOR totals, especially for larger input lists, as it runs in linear time relative to the size of the input list.


# @lc code=end
