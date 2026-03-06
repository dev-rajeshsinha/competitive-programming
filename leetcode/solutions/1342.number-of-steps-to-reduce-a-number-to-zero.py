#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
#
# algorithms
# Easy (85.75%)
# Likes:    4261
# Dislikes: 181
# Total Accepted:    904.6K
# Total Submissions: 1.1M
# Testcase Example:  '14'
#
# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.
#
#
# Example 1:
#
#
# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.
#
#
# Example 2:
#
#
# Input: num = 8
# Output: 4
# Explanation:
# Step 1) 8 is even; divide by 2 and obtain 4.
# Step 2) 4 is even; divide by 2 and obtain 2.
# Step 3) 2 is even; divide by 2 and obtain 1.
# Step 4) 1 is odd; subtract 1 and obtain 0.
#
#
# Example 3:
#
#
# Input: num = 123
# Output: 12
#
#
#
# Constraints:
#
#
# 0 <= num <= 10^6
#
#
#


# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # # The approach is to check the least significant bit of the number. If it is 0, we can divide the number by 2 (right shift). If it is 1, we need to subtract 1 from the number. We repeat this process until the number becomes 0, counting the steps taken.
        # # Time complexity: O(log n), where n is the input number. This is because in the worst case, we will be halving the number until it becomes 0.
        # # Space complexity: O(1), as we are using only a constant amount of space for the count variable.

        # # Initialize the count of steps to 0
        # count = 0

        # # Loop until the number becomes 0
        # while num > 0:
        #     # Check if the least significant bit is 0 (even number)
        #     if num & 1 == 0:
        #         # If it is even, divide the number by 2 (right shift)
        #         num >>= 1
        #     else:
        #         # If it is odd, subtract 1 from the number
        #         num -= 1

        #     # Increment the count of steps
        #     count += 1

        # # Return the total count of steps taken to reduce the number to zero
        # return count

        # There is an alternative approach to solve this problem using bit manipulation. This approach calculates the total steps by analyzing the binary representation of the number. In binary, dividing an even number by 2 is equivalent to a right bit-shift, which simply removes a '0' from the end; this takes exactly 1 step. However, subtracting 1 from an odd number changes its rightmost '1' into a '0'. Since that new '0' must then be shifted out by a division in the very next step, processing any '1' bit effectively costs 2 steps (one subtraction followed by one shift). Therefore, the total base steps equal the total number of bits (1 step per bit for the shifting) plus the total number of '1's (1 extra step per '1' for the subtractions). Finally, we subtract 1 from this total because the most significant bit (the very last '1' on the far left) only needs to be subtracted to reach 0; we do not need to perform a final shift on a number that is already 0.
        # Time complexity: O(1), as we are performing a constant number of operations to calculate the steps.
        # Space complexity: O(1), as we are using only a constant amount of space for the calculations.

        # If the number is 0, we return 0 steps. Otherwise, we calculate the steps using the formula mentioned above and return the result.
        return 0 if num == 0 else (num.bit_length() + num.bit_count() - 1)


# @lc code=end
