#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#
# https://leetcode.com/problems/concatenation-of-array/description/
#
# algorithms
# Easy (90.50%)
# Likes:    4111
# Dislikes: 450
# Total Accepted:    1.4M
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,1]'
#
# Given an integer array nums of length n, you want to create an array ans of
# length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
# (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.
#
#
# Example 1:
#
#
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
#
# Example 2:
#
#
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # We can create the concatenated array by using a list comprehension that iterates through the range of 2n (where n is the length of the input array nums) and uses the modulo operator to access the elements of nums in a cyclic manner. Specifically, for each index i in the range of 2n, we can access the corresponding element in nums using nums[i % len(nums)]. This way, when i is less than n, it will access the first n elements of nums, and when i is greater than or equal to n, it will wrap around and access the elements of nums again.
        # Time complexity: O(n), where n is the length of the input array nums, since we are creating a new array of length 2n.
        # Space complexity: O(n), since we are creating a new array of length 2n.

        # Iterate through the range of 2n and use the modulo operator to access the elements of nums in a cyclic manner
        # return [nums[i % len(nums)] for i in range(len(nums) * 2)]

        # Alternatively, we can also create the concatenated array by simply concatenating the input array nums with itself. This can be done using the + operator to concatenate the two lists. This approach is more straightforward and also has a time complexity of O(n) and space complexity of O(n), and it is more efficient than the list comprehension approach since it avoids the overhead of iterating through the range of 2n and using the modulo operator.
        # Time complexity: O(n), where n is the length of the input array nums, since we are creating a new array of length 2n.
        # Space complexity: O(n), since we are creating a new array of length 2n.

        # Concatenate the input array nums with itself
        return nums + nums


# @lc code=end
