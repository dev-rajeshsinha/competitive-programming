#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
#
# algorithms
# Medium (88.32%)
# Likes:    1505
# Dislikes: 91
# Total Accepted:    188.5K
# Total Submissions: 213.4K
# Testcase Example:  '[5,2,0,3,1]'
#
# You are given an integer array pref of size n. Find and return the array arr
# of size n that satisfies:
#
#
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
#
#
# Note that ^ denotes the bitwise-xor operation.
#
# It can be proven that the answer is unique.
#
#
# Example 1:
#
#
# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
#
#
# Example 2:
#
#
# Input: pref = [13]
# Output: [13]
# Explanation: We have pref[0] = arr[0] = 13.
#
#
#
# Constraints:
#
#
# 1 <= pref.length <= 10^5
# 0 <= pref[i] <= 10^6
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # # The approach is to iterate through the pref array and calculate the original array res using the properties of XOR. We maintain a variable current_xor that keeps track of the cumulative XOR of the elements in res up to the current index. For each index i, we can derive res[i] by XORing current_xor with pref[i], since pref[i] is the XOR of all elements in res from index 0 to i. After calculating res[i], we update current_xor by XORing it with res[i] to include the new element in our cumulative XOR for the next iteration.
        # # Time Complexity: O(n), where n is the length of the pref array, since we iterate through it once.
        # # Space Complexity: O(n), since we create a new array res to store the original array res.

        # # Initialize the result array with the same length as pref and a variable to keep track of the current XOR value.
        # res = [0] * len(pref)

        # # This variable will hold the cumulative XOR of the elements in res up to the current index.
        # current_xor = 0

        # # Iterate through the pref array to calculate the original array res.
        # for i in range(len(pref)):
        #     # Calculate res[i] using the current_xor and pref[i]. Since pref[i] is the XOR of all elements in res from index 0 to i, we can derive res[i] by XORing current_xor with pref[i].
        #     res[i] = current_xor ^ pref[i]

        #     # Update current_xor by XORing it with res[i] to include the new element in our cumulative XOR for the next iteration.
        #     current_xor ^= res[i]

        # # Return the original array res.
        # return res

        # We can also solve this problem in-place by modifying the pref array directly to store the original array res. We can iterate through the pref array from the end to the beginning, and for each index i, we can calculate pref[i] by XORing it with pref[i - 1]. This way, we can derive the original array res without using extra space for a separate result array.
        # Time Complexity: O(n), where n is the length of the pref array, since we iterate through it once.
        # Space Complexity: O(1), since we modify the pref array in-place without using extra space for a separate result array.

        # Iterate through the pref array from the end to the beginning, starting from the last index down to 1.
        for i in range(len(pref) - 1, 0, -1):
            # Calculate pref[i] by XORing it with pref[i - 1]. This way, we can derive the original array res without using extra space for a separate result array.
            pref[i] ^= pref[i - 1]

        # Return the modified pref array, which now contains the original array res.
        return pref


# @lc code=end
