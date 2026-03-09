#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (82.05%)
# Likes:    19104
# Dislikes: 340
# Total Accepted:    3M
# Total Submissions: 3.6M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # # The approach is to build the power set by recursively building subsets. For each element in the input list, we have two choices: either include it in the current subset or exclude it. We can represent these choices as a binary tree, where each level corresponds to a decision for a particular element. By traversing this tree, we can generate all possible subsets.
        # # Time Complexity: O(n*2^n) - we generate 2^n subsets and each subset takes O(n) time to copy.
        # # Space Complexity: O(n*2^n) - we store 2^n subsets and each subset can take O(n) space in the worst case.

        # # Initialize an empty list to store the power sets
        # power_sets = []

        # # Define a recursive function to build subsets by exploring both possibilities (including or excluding the current element)
        # def build_subset(current_index: int, current_subset: list[int]):
        #     # If we have considered all elements, add the current subset to the power sets
        #     if current_index == len(nums):
        #         nonlocal power_sets

        #         # Add a copy of the current subset to the power sets to avoid reference issues
        #         power_sets.append(current_subset.copy())
        #     # If we have not yet considered all elements, explore both possibilities: excluding the current element and including the current element
        #     else:
        #         # Explore the possibility of excluding the current element
        #         build_subset(current_index + 1, current_subset)

        #         # Add the current element to the subset
        #         current_subset.append(nums[current_index])

        #         # Explore the possibility of including the current element
        #         build_subset(current_index + 1, current_subset)

        #         # Remove the current element from the subset to backtrack and explore other possibilities
        #         current_subset.pop()

        # # Start building subsets from the first index with an empty subset
        # build_subset(0, [])

        # # Return the list of power sets
        # return power_sets

        # # This approach is to build the power set using bit manipulation. Each subset can be represented as a set of bits where each bit indicates whether the corresponding element in the input list is included in the subset or not. By iterating through all possible binary numbers from 0 to 2^n - 1, we can generate all subsets.
        # # Time Complexity: O(n*2^n) - we iterate through all of the n elements in the input list while building each of the 2^n subsets.
        # # Space Complexity: O(n*2^n) - we store 2^n subsets and each subset can take O(n) space in the worst case.

        # # Calculate the total number of subsets, which is 2^n (where n is the length of the input list)
        # total_number_of_subsets = 1 << len(nums)

        # # Initialize an empty list to store the power sets
        # power_sets = []

        # # Iterate through all possible binary numbers from 0 to 2^n - 1 (exclusive) to generate subsets
        # for i in range(0, total_number_of_subsets):
        #     # Initialize an empty list to store the current subset being built
        #     current_subset = []

        #     # Use a variable to keep track of the current subset mask (the binary representation of the current subset)
        #     current_subset_mask = i

        #     # Use a variable to keep track of the current index in the input array (nums) while building the current subset
        #     current_index_in_array = 0

        #     # Loop until there are still bits to process in the current subset mask
        #     while current_subset_mask > 0:
        #         # Check if the least significant bit of the current subset mask is set (i.e., if it is 1). If it is, it means that the corresponding element in the input array should be included in the current subset.
        #         if current_subset_mask & 1 == 1:
        #             # If the least significant bit is set, add the corresponding element from the input array (nums) to the current subset
        #             current_subset.append(nums[current_index_in_array])

        #         # Right shift the current subset mask to process the next bit in the next iteration of the loop
        #         current_subset_mask >>= 1

        #         # Increment the current index in the input array to move to the next element
        #         current_index_in_array += 1

        #     # After processing all bits for the current subset mask, add the current subset to the list of power sets
        #     power_sets.append(current_subset)

        # # Return the list of power sets
        # return power_sets

        # This approach is to build the power set iteratively (which is also known as Cascading). We start with an initial power set that contains only the empty subset. For each element in the input list, we take all existing subsets in the power set and create new subsets by adding the current element to them. This way, we can generate all possible subsets iteratively.
        # Time Complexity: O(n*2^n) - we iterate through all of the n elements in the input list while building each of the 2^n subsets.
        # Space Complexity: O(n*2^n) - we store 2^n subsets and each subset can take O(n) space in the worst case.

        # Initialize the power set with the empty subset
        power_sets = [[]]

        # Iterate through each number in the input list (nums)
        for num in nums:
            # For each number, we create new subsets by adding the current number to all existing subsets in the power set. We use a list comprehension to generate these new subsets and extend the power set with them.
            power_sets.extend([subset + [num] for subset in power_sets])

        # Return the list of power sets
        return power_sets


# @lc code=end
