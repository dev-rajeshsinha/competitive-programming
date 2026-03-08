#
# @lc app=leetcode id=1829 lang=python3
#
# [1829] Maximum XOR for Each Query
#
# https://leetcode.com/problems/maximum-xor-for-each-query/description/
#
# algorithms
# Medium (84.76%)
# Likes:    1264
# Dislikes: 194
# Total Accepted:    144.4K
# Total Submissions: 170.3K
# Testcase Example:  '[0,1,1,3]\n2'
#
# You are given a sorted array nums of n non-negative integers and an integer
# maximumBit. You want to perform the following query n times:
#
#
# Find a non-negative integer k < 2^maximumBit such that nums[0] XOR nums[1]
# XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the
# i^th query.
# Remove the last element from the current array nums.
#
#
# Return an array answer, where answer[i] is the answer to the i^th query.
#
#
# Example 1:
#
#
# Input: nums = [0,1,1,3], maximumBit = 2
# Output: [0,3,2,3]
# Explanation: The queries are answered as follows:
# 1^st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
# 2^nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
# 3^rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
# 4^th query: nums = [0], k = 3 since 0 XOR 3 = 3.
#
#
# Example 2:
#
#
# Input: nums = [2,3,4,7], maximumBit = 3
# Output: [5,2,6,5]
# Explanation: The queries are answered as follows:
# 1^st query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
# 2^nd query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
# 3^rd query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
# 4^th query: nums = [2], k = 5 since 2 XOR 5 = 7.
#
#
# Example 3:
#
#
# Input: nums = [0,1,2,2,5,7], maximumBit = 3
# Output: [4,3,6,4,6,7]
#
#
#
# Constraints:
#
#
# nums.length == n
# 1 <= n <= 10^5
# 1 <= maximumBit <= 20
# 0 <= nums[i] < 2^maximumBit
# nums​​​ is sorted in ascending order.
#
#
#

# @lc code=start
from typing import List
from itertools import accumulate
from operator import xor


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # # This approach is based on the XOR properties. For a given running XOR sum 'X', we need to find a number 'k' (strictly less
        # # than 2^maximumBit) such that `X ^ k` is as large as possible. To achieve this, 'k' needs to perfectly flip all the 0s in 'X' to 1s.

        # # Step 1: Generating the Mask
        # # The absolute maximum value we can ever achieve with `maximumBit` bits is a binary number made entirely of 1s (e.g., if maximumBit is 3, the max is 111). We generate this "ideal maximum" mask mathematically: `(1 << maximumBit) - 1`.

        # # Step 2: The XOR Inverse Property
        # # Our dream equation is: `X ^ k = mask`. Because the XOR operator is its own inverse, we can swap variables across the equals sign to solve for 'k' directly: `k = mask ^ X`

        # # Step 3: The Single-Pass Pipeline
        # # As we iterate through the array, we maintain a running XOR sum ('X'). At each step, we simply calculate `mask ^ X` to instantly find the optimal 'k' without any inner loops. We populate the answer array in reverse order to simulate the elements being removed from the end of the array.
        # # Time Complexity: O(n) - We traverse the array once to compute the running XOR and fill the answer array.
        # # Space Complexity: O(n) - We use an answer array of the same size as the input array to store the results.

        # # Calculate the length of the input array
        # n = len(nums)

        # # Generate the mask which is the maximum possible XOR value with maximumBit bits (2^maximumBit - 1)
        # mask = (1 << maximumBit) - 1

        # # Initialize the answer array with zeros to store the results of each query
        # ans = [0] * n

        # # Initialize a variable to keep track of the cumulative XOR of the elements processed so far
        # xor_till_current_element = 0

        # # Iterate through the input array from index 0 to n-1
        # for index, num in enumerate(nums):
        #     # Update the cumulative XOR with the current number from the array to get the XOR of all elements up to the current index
        #     xor_till_current_element ^= num

        #     # Calculate the optimal 'k' for the current query using the XOR inverse property and store it in the answer array in reverse order to simulate the removal of elements from the end of the array
        #     ans[n - 1 - index] = xor_till_current_element ^ mask

        # # Return the answer array containing the results for each query
        # return ans

        # There is another way to implement the same logic using the `accumulate` function from the `itertools` module, which can simplify the code and make it more concise. The `accumulate` function can be used to compute the running XOR of the elements in the `nums` array, which then can be appended to a list in reverse order, while applying the XOR between the mask and each element of the list to get the optimal 'k' for each query.
        # Time Complexity: O(n) - We traverse the array once to compute the running XOR and fill the answer array.
        # Space Complexity: O(n) - We use an answer array of the same size as the input array to store the results. Also, the `list(accumulate(nums, xor))` creates an additional list of size n to store the cumulative XOR values.

        # Generate the mask which is the maximum possible XOR value with maximumBit bits (2^maximumBit - 1)
        mask = (1 << maximumBit) - 1

        # Accumulate the XOR values of the `nums` array and reverse the list to simulate the removal of elements from the end of the array. For each prefix XOR value, calculate the optimal 'k' using the XOR inverse property and return the list of results.
        return [
            prefix_xor ^ mask for prefix_xor in reversed(list(accumulate(nums, xor)))
        ]


# @lc code=end
