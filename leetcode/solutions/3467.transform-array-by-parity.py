#
# @lc app=leetcode id=3467 lang=python3
#
# [3467] Transform Array by Parity
#
# https://leetcode.com/problems/transform-array-by-parity/description/
#
# algorithms
# Easy (89.75%)
# Likes:    101
# Dislikes: 7
# Total Accepted:    90K
# Total Submissions: 100.3K
# Testcase Example:  '[4,3,2,1]'
#
# You are given an integer array nums. Transform nums by performing the
# following operations in the exact order specified:
#
#
# Replace each even number with 0.
# Replace each odd numbers with 1.
# Sort the modified array in non-decreasing order.
#
#
# Return the resulting array after performing these operations.
#
#
# Example 1:
#
#
# Input: nums = [4,3,2,1]
#
# Output: [0,0,1,1]
#
# Explanation:
#
#
# Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with
# 1. Now, nums = [0, 1, 0, 1].
# After sorting nums in non-descending order, nums = [0, 0, 1, 1].
#
#
#
# Example 2:
#
#
# Input: nums = [1,5,1,4,2]
#
# Output: [0,0,1,1,1]
#
# Explanation:
#
#
# Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1)
# with 1. Now, nums = [1, 1, 1, 0, 0].
# After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # The approach is to count the number of even elements in the array and then replace the first count_of_even_elements with 0 and the rest with 1. Finally, we return the modified array.
        # Time complexity: O(n), where n is the length of the input array. We iterate through the array once to count the number of even elements and then iterate through the array again to modify the elements based on the count of even elements.
        # Space complexity: O(1), as we are modifying the input array in place and not using any additional data structures that grow with the size of the input.

        # Count the number of even elements in the input array
        count_of_even_elements = sum(num & 1 == 0 for num in nums)

        # Iterate through the input array and replace the first count_of_even_elements with 0 and the rest with 1
        for i in range(len(nums)):
            # If there are still even elements to replace, replace the current element with 0 and decrement the count of even elements.
            if count_of_even_elements > 0:
                nums[i] = 0
                count_of_even_elements -= 1
            # If there are no more even elements to replace, replace the current element with 1.
            else:
                nums[i] = 1

        # Return the modified array after performing the operations
        return nums


# @lc code=end
