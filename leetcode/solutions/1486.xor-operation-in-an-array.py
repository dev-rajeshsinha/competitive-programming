#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#
# https://leetcode.com/problems/xor-operation-in-an-array/description/
#
# algorithms
# Easy (87.43%)
# Likes:    1503
# Dislikes: 340
# Total Accepted:    263.3K
# Total Submissions: 301.1K
# Testcase Example:  '5\n0'
#
# You are given an integer n and an integer start.
#
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n ==
# nums.length.
#
# Return the bitwise XOR of all elements of nums.
#
#
# Example 1:
#
#
# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8)
# = 8.
# Where "^" corresponds to bitwise XOR operator.
#
#
# Example 2:
#
#
# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) =
# 8.
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length
#
#
#


# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # # The approach is to iterate through the values between 0 and n - 1, calculate the value of start + (2 * index) and XOR it with the result. Finally, return the result.
        # # Time complexity: O(n) where n is the length of the array nums.
        # # Space complexity: O(1) since we are using only a constant amount of space to store the result.

        # # Initialize the result variable to store the XOR of all elements in the array.
        # result = 0

        # # Iterate through the values between 0 and n - 1
        # for index in range(0, n):
        #     # Calculate the value of start + (2 * index) and XOR it with the result.
        #     result ^= start + (2 * index)

        # # Return the result
        # return result

        # The above approach is straightforward but can be optimized using mathematical properties of XOR and the structure of the array. The conceptual array jumps by 2: [start, start + 2, start + 4...]. Instead of simulating the array in O(n) time, we use the following mathematical properties:

        # 1. Make it Consecutive (>> 1): By dividing the start number by 2 (right-shift), we conceptually turn our jumping sequence into a sequence of consecutive integers, which is [start // 2, (start // 2) + 1, (start // 2) + 2, ...].

        # 2. The Range XOR Trick: The XOR sum of consecutive integers starting from 0 repeats in a predictable pattern every 4 numbers. We find the XOR of our specific range using the formula: XOR(0 to end) ^ XOR(0 to start - 1).

        # 3. Restore Magnitude (<< 1): We multiply our calculated XOR sum back by 2 (left-shift) to undo the division from Step 1.

        # 4. Restore the 1s Bit: Shifting threw away the least significant bit (the odd/even flag). Because we jump by 2, all numbers share the same 1s bit as 'start'. The final XORed 1s bit is '1' ONLY if both 'start' is odd AND 'n' (the count of numbers) is odd. We use bitwise OR (|) to safely glue this missing bit back onto the end.

        # Time complexity: O(1) since we are using a constant number of operations to calculate the XOR.
        # Space complexity: O(1) since we are using only a constant amount of space

        # Helper function to calculate the XOR of all numbers from 0 to n
        def calculate_xor_from_zero_to(n) -> int:
            # The XOR of all numbers from 0 to n follows a pattern based on n mod 4:
            # n % 4 == 0 -> n
            # n % 4 == 1 -> 1
            # n % 4 == 2 -> n + 1
            # n % 4 == 3 -> 0
            return n if n % 4 == 0 else 1 if n % 4 == 1 else n + 1 if n % 4 == 2 else 0

        # Calculate the XOR of the range of numbers corresponding to the array elements, then shift left to restore magnitude.
        total_xor = (
            calculate_xor_from_zero_to((start >> 1) + (n - 1))
            ^ calculate_xor_from_zero_to((start >> 1) - 1)
        ) << 1

        # Restore the 1s bit if both 'start' and 'n' are odd and return the final result.
        return total_xor | ((start & 1) & (n & 1))


# @lc code=end
