#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
#
# algorithms
# Medium (89.56%)
# Likes:    1403
# Dislikes: 97
# Total Accepted:    247.7K
# Total Submissions: 276.5K
# Testcase Example:  '[3,1]'
#
# Given an integer array nums, find the maximum possible bitwise OR of a subset
# of nums and return the number of different non-empty subsets with the maximum
# bitwise OR.
#
# An array a is a subset of an array b if a can be obtained from b by deleting
# some (possibly zero) elements of b. Two subsets are considered different if
# the indices of the elements chosen are different.
#
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length -
# 1] (0-indexed).
#
#
# Example 1:
#
#
# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2
# subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There
# are 2^3 - 1 = 7 total subsets.
#
#
# Example 3:
#
#
# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6
# subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 16
# 1 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # The approach is to first calculate the maximum bitwise OR, which is the bitwise OR of all the numbers in the array. Then, we can use a recursive function to count the number of subsets that have a bitwise OR equal to the maximum bitwise OR. We can use memoization to optimize the recursive function and avoid redundant calculations.
        # Time complexity: O(n*maximum_bitwise_or), where n is the length of the input array and maximum_bitwise_or is the maximum bitwise OR value.
        # Space complexity: O(n*maximum_bitwise_or) for the cache used in memoization.

        # Initialize the maximum bitwise OR to 0
        maximum_bitwise_or = 0

        # Calculate the maximum bitwise OR by iterating through the input array and performing a bitwise OR operation with each number
        for num in nums:
            maximum_bitwise_or |= num

        # Initialize a cache to store the results of previously computed subproblems for memoization
        cache: dict[tuple[int, int], int] = {}

        # Define a recursive function to count the number of subsets that have a bitwise OR equal to the maximum bitwise OR
        def count_subsets(current_index: int, current_or: int) -> int:
            # Use the nonlocal keyword to access the variables defined in the outer scope of the count_subsets function
            nonlocal nums, maximum_bitwise_or, cache

            # Base case: If we have reached the end of the input array, check if the current bitwise OR is equal to the maximum bitwise OR. If it is, return 1 (indicating that we found a valid subset), otherwise return 0.
            if current_index == len(nums):
                return 1 if current_or == maximum_bitwise_or else 0

            # Check if the result for the current index and current bitwise OR is already computed and stored in the cache. If it is, return the cached result to avoid redundant calculations.
            if (current_index, current_or) in cache:
                return cache[(current_index, current_or)]

            # If the current bitwise OR is already equal to the maximum bitwise OR, we can return the number of subsets that can be formed with the remaining elements in the input array, which is 2^(number of remaining elements) since each element can either be included or excluded from the subset.
            if current_or == maximum_bitwise_or:
                return 1 << (len(nums) - current_index)

            # Calculate the number of subsets by recursively calling the count_subsets function for both cases: including the current number in the subset (which updates the current bitwise OR) and excluding the current number from the subset (which keeps the current bitwise OR unchanged). The total count is the sum of both cases. Store the result in the cache before returning it to optimize future calls with the same parameters.
            cache[(current_index, current_or)] = count_subsets(
                current_index + 1, current_or
            ) + count_subsets(current_index + 1, current_or | nums[current_index])

            # Return the computed result for the current index and current bitwise OR from the cache
            return cache[(current_index, current_or)]

        # Start the recursive function with the initial index of 0 and an initial bitwise OR of 0
        return count_subsets(0, 0)


# @lc code=end
