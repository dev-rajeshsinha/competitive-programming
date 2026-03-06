#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
#
# algorithms
# Medium (86.98%)
# Likes:    1154
# Dislikes: 74
# Total Accepted:    235.9K
# Total Submissions: 271.3K
# Testcase Example:  '[1,3,2,4]\n[3,1,2,4]'
#
# You are given two 0-indexed integer permutations A and B of length n.
#
# A prefix common array of A and B is an array C such that C[i] is equal to the
# count of numbers that are present at or before the index i in both A and B.
#
# Return the prefix common array of A and B.
#
# A sequence of n integers is called a permutation if it contains all integers
# from 1 to n exactly once.
#
#
# Example 1:
#
#
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
#
#
# Example 2:
#
#
# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
#
#
#
# Constraints:
#
#
# 1 <= A.length == B.length == n <= 50
# 1 <= A[i], B[i] <= n
# It is guaranteed that A and B are both a permutation of n integers.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # # This approach is based on the fact that A and B are permutations of n integers, so we can use a set to keep track of the unique numbers we have seen so far. We iterate through both arrays simultaneously and count the common numbers at each index. If the numbers at the current index are the same, we increment the count. Otherwise, we check if either number has been seen before (in the unique set) and update the count accordingly. Finally, we store the count in array B and return it as the result.
        # # Time complexity: O(n), where n is the length of the input arrays A and B. We iterate through both arrays once.
        # # Space complexity: O(n), in the worst case, we may store all unique numbers in the set if all numbers are different at each index.

        # # Store the length of the input arrays
        # n = len(A)

        # # Initialize a set to keep track of unique numbers seen so far
        # unique_set: set[int] = set()

        # # Initialize a count variable to keep track of the number of common elements
        # count = 0

        # # Iterate through the indexes of the input arrays
        # for index in range(0, n):
        #     # If the numbers at the current index are the same, increment the count
        #     # We don't need to add the number to the unique set in this case, as it is already common and the same number will not be present in the given arrays at any other index, because A and B are permutations.
        #     if A[index] == B[index]:
        #         count += 1
        #     # If the numbers at the current index are different, check if either number has been seen before in the unique set and update the count accordingly.
        #     else:
        #         if A[index] in unique_set:
        #             count += 1
        #         if B[index] in unique_set:
        #             count += 1

        #         # Add the current numbers from both arrays to the unique set for future reference
        #         unique_set.add(A[index])
        #         unique_set.add(B[index])

        #     # Store the count of common elements at the current index in array B
        #     B[index] = count

        # # Return the modified array B, which now contains the prefix common counts
        # return B

        # There is an alternative approach that uses bit manipulation to keep track of the numbers seen in both arrays. We can use two integers to represent the sets of numbers seen in A and B, where each bit corresponds to a number from 1 to n. We iterate through both arrays simultaneously, updating the bitmasks for A and B, and then calculate the count of common numbers by performing a bitwise AND operation on the two bitmasks and counting the number of set bits in the result.
        # Time complexity: O(n), where n is the length of the input arrays A and B. We iterate through both arrays once.
        # Space complexity: O(1), we use only a constant amount of extra space to store the bitmasks and the count.

        # Initialize two integers to represent the sets of numbers seen in A and B
        seen_in_A = 0
        seen_in_B = 0

        # Store the length of the input arrays
        n = len(A)

        # Iterate through the indexes of the input arrays
        for index in range(0, n):
            # Update the bitmasks for A and B by setting the bit corresponding to the current number in A and B. We use a left shift operation to set the bit at the position corresponding to the number (A[index] or B[index]) in the respective bitmask.
            seen_in_A |= 1 << A[index]
            seen_in_B |= 1 << B[index]

            # Calculate the count of common numbers by performing a bitwise AND operation on the two bitmasks and counting the number of set bits in the result. The bitwise AND operation will give us a bitmask where only the bits corresponding to the common numbers are set. We can then use the bit_count() method to count the number of set bits, which will give us the count of common numbers at the current index. Finally, we store this count in array B at the current index.
            B[index] = (seen_in_A & seen_in_B).bit_count()

        # Return the modified array B, which now contains the prefix common counts
        return B


# @lc code=end
