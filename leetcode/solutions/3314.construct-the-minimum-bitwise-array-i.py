#
# @lc app=leetcode id=3314 lang=python3
#
# [3314] Construct the Minimum Bitwise Array I
#
# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/
#
# algorithms
# Easy (85.28%)
# Likes:    414
# Dislikes: 52
# Total Accepted:    135.7K
# Total Submissions: 159.1K
# Testcase Example:  '[2,3,5,7]'
#
# You are given an array nums consisting of n prime integers.
#
# You need to construct an array ans of length n, such that, for each index i,
# the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR
# (ans[i] + 1) == nums[i].
#
# Additionally, you must minimize each value of ans[i] in the resulting array.
#
# If it is not possible to find such a value for ans[i] that satisfies the
# condition, then set ans[i] = -1.
#
#
# Example 1:
#
#
# Input: nums = [2,3,5,7]
#
# Output: [-1,1,4,3]
#
# Explanation:
#
#
# For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] +
# 1) = 2, so ans[0] = -1.
# For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is
# 1, because 1 OR (1 + 1) = 3.
# For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is
# 4, because 4 OR (4 + 1) = 5.
# For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is
# 3, because 3 OR (3 + 1) = 7.
#
#
#
# Example 2:
#
#
# Input: nums = [11,13,31]
#
# Output: [9,12,15]
#
# Explanation:
#
#
# For i = 0, the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is
# 9, because 9 OR (9 + 1) = 11.
# For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is
# 12, because 12 OR (12 + 1) = 13.
# For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is
# 15, because 15 OR (15 + 1) = 31.
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 2 <= nums[i] <= 1000
# nums[i] is a prime number.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # # This approach is based on the fact that for any integer i, the expression i OR (i + 1) will set all the bits to 1 from the least significant bit up to the most significant bit of i. Therefore, to find the minimum value of ans[i] such that ans[i] OR (ans[i] + 1) equals nums[i], we can iterate through all integers starting from 0 up to nums[i] (exclusive) and check if the condition holds. If it does, we can append that integer to the result list. If we exhaust all possibilities without finding a valid integer, we append -1 to the result list.
        # # Time complexity: O(n * m), where n is the length of the input array and m is the maximum value in the input array. In the worst case, we may need to check all integers from 0 to nums[i] for each element in the input array.
        # # Space complexity: O(n), where n is the length of the input array, as we are storing the result in a new list.

        # # Initialize an empty list to store the results
        # res: List[int] = []

        # # Iterate through each number in the input array
        # for num in nums:
        #     # Iterate through integers starting from 0 up to num (exclusive)
        #     for i in range(0, num):
        #         # Check if the bitwise OR of i and (i + 1) equals num
        #         if i | (i + 1) == num:
        #             # If the condition is satisfied, append i to the result list and break out of the loop
        #             res.append(i)
        #             break
        #     # If we exhaust all possibilities without finding a valid integer, append -1 to the result list
        #     else:
        #         res.append(-1)

        # # Return the result list
        # return res

        # This is an alternate, optimized approach that reverse-engineers the operation x | (x + 1) = num in O(1) time using bitwise manipulation. The expression x | (x + 1) mathematically guarantees an odd result because it finds the rightmost '0' in x and flips it to a '1', leaving any trailing '1's intact. Because of this rule, if num is even (like 2), no valid x can exist, so we immediately return -1. For any valid odd num, the bit that was flipped from '0' to '1' is always the highest '1' within the rightmost continuous block of '1's. To find and undo this flip, we first isolate the rightmost '0' in num using the Two's Complement trick on the inverted number: (~num & -(~num)). This isolates the bit immediately to the left of our target. We then shift this isolated bit one position to the right (>> 1) to perfectly align with the bit that was changed. Finally, we use XOR (^) to flip that specific '1' back to a '0' in the original num, instantly recovering the minimum possible value of x without a single loop.
        # The expression num ^ ((~num & -(~num)) >> 1) works as follows:
        # 1. ~num: This computes the bitwise NOT of num, flipping all bits.
        # 2. -(~num): This computes the two's complement of ~num
        # 3. ~num & -(~num): This isolates the rightmost '0' bit in num, giving us a number that has only that bit set to '1'.
        # 4. ((~num & -(~num)) >> 1): This shifts the isolated bit one position to the right, aligning it with the bit that was flipped from '0' to '1' in the original num.
        # 5. num ^ ((~num & -(~num)) >> 1): This XOR operation flips the specific '1' bit back to '0' in num, effectively recovering the minimum possible value of x that satisfies the condition x OR (x + 1) = num.
        # Time complexity: O(n), where n is the length of the input array, as we are processing each element in the input array once.
        # Space complexity: O(n), where n is the length of the input array, as we are storing the result in a new list.

        # Return a list comprehension that computes the result for each number in the input array
        return [-1 if num == 2 else (num ^ ((~num & -(~num)) >> 1)) for num in nums]


# @lc code=end
