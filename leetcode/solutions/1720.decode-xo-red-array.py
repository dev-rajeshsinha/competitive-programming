#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#
# https://leetcode.com/problems/decode-xored-array/description/
#
# algorithms
# Easy (87.32%)
# Likes:    1668
# Dislikes: 221
# Total Accepted:    189.6K
# Total Submissions: 217.1K
# Testcase Example:  '[1,2,3]\n1'
#
# There is a hidden integer array arr that consists of n non-negative
# integers.
#
# It was encoded into another integer array encoded of length n - 1, such that
# encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then
# encoded = [1,2,3].
#
# You are given the encoded array. You are also given an integer first, that is
# the first element of arr, i.e. arr[0].
#
# Return the original array arr. It can be proved that the answer exists and is
# unique.
#
#
# Example 1:
#
#
# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR
# 2, 2 XOR 1] = [1,2,3]
#
#
# Example 2:
#
#
# Input: encoded = [6,2,7,3], first = 4
# Output: [4,2,0,7,4]
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^4
# encoded.length == n - 1
# 0 <= encoded[i] <= 10^5
# 0 <= first <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:

    def decode(self, encoded: List[int], first: int) -> List[int]:
        # The approach is to insert the first element at the beginning of the encoded array and then iterate through the array, applying the XOR operation between the current element and the previous element to decode the original array.
        # Time complexity: O(n), where n is the length of the encoded array.
        # Space complexity: O(1), since we are modifying the encoded array in place and not using any additional data structures.

        # Insert the first element at the beginning of the encoded array
        encoded.insert(0, first)

        # Extract the length of the encoded array after inserting the first element
        n = len(encoded)

        # Iterate through the encoded array starting from the second element till the end
        for index in range(1, n):
            # Update the current element by applying the XOR operation with the previous element
            encoded[index] ^= encoded[index - 1]

        # Return the modified encoded array, which now contains the original array
        return encoded


# @lc code=end
