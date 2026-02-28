#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
#
# algorithms
# Easy (89.89%)
# Likes:    521
# Dislikes: 22
# Total Accepted:    247.7K
# Total Submissions: 275.6K
# Testcase Example:  '[0,1,1,0]'
#
# In the town of Digitville, there was a list of numbers called nums containing
# integers from 0 to n - 1. Each number was supposed to appear exactly once in
# the list, however, two mischievous numbers sneaked in an additional time,
# making the list longer than usual.
#
# As the town detective, your task is to find these two sneaky numbers. Return
# an array of size two containing the two numbers (in any order), so peace can
# return to Digitville.
#
#
# Example 1:
#
#
# Input: nums = [0,1,1,0]
#
# Output: [0,1]
#
# Explanation:
#
# The numbers 0 and 1 each appear twice in the array.
#
#
# Example 2:
#
#
# Input: nums = [0,3,2,1,3,2]
#
# Output: [2,3]
#
# Explanation:
#
# The numbers 2 and 3 each appear twice in the array.
#
#
# Example 3:
#
#
# Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]
#
# Output: [4,5]
#
# Explanation:
#
# The numbers 4 and 5 each appear twice in the array.
#
#
#
# Constraints:
#
#
# 2 <= n <= 100
# nums.length == n + 2
# 0 <= nums[i] < n
# The input is generated such that nums contains exactly two repeated
# elements.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # # The approach is to use a dictionary to count the occurrences of each number in the input list. We will iterate through the list and update the count for each number. After counting, we will iterate through the dictionary and collect the numbers that have a count greater than 1, which are the two sneaky numbers.
        # # Time complexity: O(n) where n is the length of the input list, since we are iterating through the list and the dictionary.
        # # Space complexity: O(n) for the dictionary to store the counts of each number.

        # # Initialize a dictionary to store the counts of each number.
        # count_dict: dict[int, int] = {}

        # # Iterate through the input list
        # for num in nums:
        #     # Update the count for the current number in the dictionary
        #     count_dict[num] = count_dict.get(num, 0) + 1

        # # Collect the numbers that have a count greater than 1 in a list, and return it.
        # return [key for key, value in count_dict.items() if value > 1]

        # There is also another more optimal approach that uses the properties of XOR operation. We can XOR all the numbers in the input list and XOR it with all the numbers from 0 to n-1. The result will be the XOR of the two sneaky numbers. Then we can find a set bit in the result and use it to partition the numbers into two groups, which will help us find the two sneaky numbers.
        # Time complexity: O(n) where n is the length of the input list, since we are iterating through the list and the range of numbers.
        # Space complexity: O(1) since we are using a constant amount of space.

        # Calculate the total expected elements in the list, which is n (the length of the input list) minus 2 (the two sneaky numbers).
        total_expected_elements = len(nums) - 2

        # Initialize total_xor to 0 where we will store the XOR of all numbers in the input list and the XOR of all numbers from 0 to n-1.
        total_xor = 0

        # XOR all numbers from 0 to n-1 and store the result in total_xor.
        for i in range(0, total_expected_elements):
            total_xor ^= i

        # XOR all numbers in the input list and store the result in total_xor.
        # After this step, total_xor will be the XOR of the two sneaky numbers.
        for num in nums:
            total_xor ^= num

        # Perform a bitwise AND between total_xor and its negation to find the rightmost set bit,
        # which will be used to partition the numbers into two groups.
        separator = total_xor & (-total_xor)

        # Initialize two variables to store the XOR of the two groups of numbers.
        first_group = second_group = 0

        # Partition the numbers from 0 to n-1 into two groups based on the separator bit and XOR the numbers in each group.
        for i in range(0, total_expected_elements):
            if i & separator == 0:
                first_group ^= i
            else:
                second_group ^= i

        # Partition the numbers in the input list into two groups based on the separator bit and XOR the numbers in each group.
        for num in nums:
            if num & separator == 0:
                first_group ^= num
            else:
                second_group ^= num

        # Combine the results from both groups (which will be the two sneaky numbers) and return them in a list.
        return [first_group, second_group]


# @lc code=end
