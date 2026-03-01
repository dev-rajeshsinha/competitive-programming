#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
# https://leetcode.com/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (89.78%)
# Likes:    5850
# Dislikes: 286
# Total Accepted:    1M
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,1,1,3]'
#
# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: 0
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
from collections import Counter
from math import comb


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # The approach is to count the frequency of each number in the input list and then calculate the number of good pairs using the formula n * (n - 1) / 2, where n is the frequency of a particular number. This formula works because if there are n occurrences of a number, we can choose any 2 of them to form a good pair, which is given by the combination formula C(n, 2) = n! / (2! * (n - 2)!) = n * (n - 1) / 2.
        # Time complexity: O(n), where n is the length of the input list. We iterate through the list once to count the frequencies and then iterate through the list of values in the frequency dictionary once to calculate the number of good pairs.
        # Space complexity: O(n) in the worst case, where n is the length of the input list. This happens when all numbers in the list are unique, and we need to store each number in the frequency dictionary.

        # # Create a frequency dictionary to count the occurrences of each number in the input list
        # frequency_dict = {}

        # # Iterate through the input list and populate the frequency dictionary
        # for num in nums:
        #     frequency_dict[num] = frequency_dict.get(num, 0) + 1

        # # Initialize a variable to keep track of the total number of good pairs
        # total_number_of_good_pairs = 0

        # # Iterate through the values in the frequency dictionary and calculate the number of good pairs for each number using the formula n * (n - 1) / 2
        # for value in frequency_dict.values():
        #     total_number_of_good_pairs += (value * (value - 1)) // 2

        # # Return the total number of good pairs
        # return total_number_of_good_pairs

        # We can also solve the problem in a single pass through the input list by keeping track of the frequency of each number as we iterate through the list and calculating the number of good pairs on the fly. This way, we can avoid the need for a separate loop to calculate the number of good pairs after counting the frequencies. For example, if we encounter number x and it has already been seen k times before, then we can form k good pairs with the current occurrence of x, and next we can update the frequency of x in the frequency dictionary accordingly. In that way, we can calculate the total number of good pairs in a single pass through the input list, which has a time complexity of O(n) and a space complexity of O(n) in the worst case.

        # # Create a frequency dictionary to count the occurrences of each number in the input list
        # frequency_dict = {}

        # # Initialize a variable to keep track of the total number of good pairs
        # pairs = 0

        # # Iterate through the input list and calculate the number of good pairs on the fly while populating the frequency dictionary
        # for num in nums:
        #     pairs += frequency_dict.get(num, 0)
        #     frequency_dict[num] = frequency_dict.get(num, 0) + 1

        # # Return the total number of good pairs
        # return pairs

        # We can achieve the same result in a more concise way by using the Counter class from the collections module to count the frequencies of each number and then using the `comb` function from the math module to calculate the number of combinations of 2 items from a set of n items, which is equivalent to the formula n * (n - 1) / 2. Finally, we can sum up the results for all unique numbers in the input list to get the total number of good pairs and return that value.
        return sum([comb(count, 2) for count in Counter(nums).values()])


# @lc code=end
