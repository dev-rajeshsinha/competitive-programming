#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
#
# algorithms
# Easy (87.81%)
# Likes:    1595
# Dislikes: 37
# Total Accepted:    363.8K
# Total Submissions: 414.2K
# Testcase Example:  '10\n7'
#
# A bit flip of a number x is choosing a bit in the binary representation of x
# and flipping it from either 0 to 1 or 1 to 0.
#
#
# For example, for x = 7, the binary representation is 111 and we may choose
# any bit (including any leading zeros not shown) and flip it. We can flip the
# first bit from the right to get 110, flip the second bit from the right to
# get 101, flip the fifth bit from the right (a leading zero) to get 10111,
# etc.
#
#
# Given two integers start and goal, return the minimum number of bit flips to
# convert start to goal.
#
#
# Example 1:
#
#
# Input: start = 10, goal = 7
# Output: 3
# Explanation: The binary representation of 10 and 7 are 1010 and 0111
# respectively. We can convert 10 to 7 in 3 steps:
# - Flip the first bit from the right: 1010 -> 1011.
# - Flip the third bit from the right: 1011 -> 1111.
# - Flip the fourth bit from the right: 1111 -> 0111.
# It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we
# return 3.
#
# Example 2:
#
#
# Input: start = 3, goal = 4
# Output: 3
# Explanation: The binary representation of 3 and 4 are 011 and 100
# respectively. We can convert 3 to 4 in 3 steps:
# - Flip the first bit from the right: 011 -> 010.
# - Flip the second bit from the right: 010 -> 000.
# - Flip the third bit from the right: 000 -> 100.
# It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we
# return 3.
#
#
#
# Constraints:
#
#
# 0 <= start, goal <= 10^9
#
#
#
# Note: This question is the same as 461: Hamming Distance.
#
#


# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # The approach is to find the number of bits that are different between start and goal. We can do this by performing a bitwise XOR operation between start and goal, which will give us a number where each bit is 1 if the corresponding bits of start and goal are different, and 0 if they are the same. Then, we can count the number of 1s in the result to get the number of bit flips needed.
        # Time complexity: O(start^goal) since we are looping the number of bits in the result of the XOR operation, till it is greater than 0.
        # Space complexity: O(1) since we are using a constant amount of space to store the count and the bit difference.

        # If we are using Brian Kernighan's algorithm to count the number of set bits, the time complexity would be O(k) where k is the number of set bits in the bit difference, which can be much less than the total number of bits.

        # Calculate the bit difference using XOR
        bit_difference = start ^ goal

        # Initialize count variable to count the number of bit flips
        count = 0

        # Loop until there are no more 1s in the bit difference
        while bit_difference > 0:
            # Increment count if the least significant bit is 1
            count += 1

            # Right shift the bits to check the next bit
            # Right shifting the bits one by one will cause the loop to run for those many times as the position of the highest set bit in the bit difference. In the worst case, if start and goal differ in all bits, the loop will run for the number of bits in the binary representation of the numbers, which is at most 30 for numbers up to 10^9.
            # bit_difference >>= 1

            # A more efficient way to count the number of 1s in the bit difference is to use Brian Kernighan's algorithm, which repeatedly flips the least significant set bit until the number becomes zero. This way, we only loop for the number of set bits in the bit difference, which can be much less than the total number of bits.
            bit_difference &= bit_difference - 1

        # Rather than using the while loop, we could also use the built-in function `bit_count()` in Python 3.10 and above to count the number of 1s in the bit difference directly:
        # count = bit_difference.bit_count()

        # Return the total count of bit flips needed
        return count


# @lc code=end
