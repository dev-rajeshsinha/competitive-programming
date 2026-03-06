#
# @lc app=leetcode id=3211 lang=python3
#
# [3211] Generate Binary Strings Without Adjacent Zeros
#
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/
#
# algorithms
# Medium (88.25%)
# Likes:    280
# Dislikes: 49
# Total Accepted:    79K
# Total Submissions: 89.6K
# Testcase Example:  '3'
#
# You are given a positive integer n.
#
# A binary string x is valid if all substrings of x of length 2 contain at
# least one "1".
#
# Return all valid strings with length n, in any order.
#
#
# Example 1:
#
#
# Input: n = 3
#
# Output: ["010","011","101","110","111"]
#
# Explanation:
#
# The valid strings of length 3 are: "010", "011", "101", "110", and "111".
#
#
# Example 2:
#
#
# Input: n = 1
#
# Output: ["0","1"]
#
# Explanation:
#
# The valid strings of length 1 are: "0" and "1".
#
#
#
# Constraints:
#
#
# 1 <= n <= 18
#
#
#

# @lc code=start
from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        # # The approach is to use backtracking to generate all possible binary strings of length n, while ensuring that no two adjacent zeros are present. We start with an empty string and at each step, we can either add a "0" or a "1". However, if the last character added was a "0", we can only add a "1" next to avoid adjacent zeros. We continue this process until we reach the desired length n, at which point we add the valid string to our result list.
        # # Time complexity: O(n*2^n) in the worst case, as we are generating all possible binary strings of length n and each string takes O(n) time to construct each string from the list of characters using the join operation where n is the length of the string.
        # # Space complexity: O(n*2^n) in the worst case, as we are storing all valid binary strings (total 2^n) of length n in the result list, and each string takes O(n) space to store where n is the length of the string.

        # # Initialize an empty list to store the valid binary strings
        # result: List[str] = []

        # # Define a recursive function to generate valid binary strings
        # def create_valid_strings(current_string_list: List[str]):
        #     # Use the nonlocal keyword to indicate that we want to modify the result variable defined in the outer scope
        #     nonlocal result

        #     # If the current string list has not reached the desired length n, we can continue to add characters
        #     if len(current_string_list) < n:
        #         # If the last character added was "0", we can only add "1" next to avoid adjacent zeros
        #         if current_string_list[-1] == "0":
        #             # Append "1" to the current string list and recursively call the function to continue building the string
        #             current_string_list.append("1")
        #             create_valid_strings(current_string_list)

        #             # After the recursive call returns, we remove the last character to backtrack and explore other possibilities
        #             current_string_list.pop()
        #         else:
        #             # If the last character was "1", we can add either "0" or "1" next. We first add "0" and recursively call the function to continue building the string
        #             current_string_list.append("0")
        #             create_valid_strings(current_string_list)

        #             # After the recursive call returns, we remove the last character to backtrack and explore other possibilities
        #             current_string_list.pop()

        #             # Next, we add "1" and recursively call the function to continue building the string
        #             current_string_list.append("1")
        #             create_valid_strings(current_string_list)

        #             # After the recursive call returns, we remove the last character to backtrack and explore other possibilities
        #             current_string_list.pop()
        #     else:
        #         # If the current string list has reached the desired length n, we add the valid string to the result list by joining the characters in the current string list and appending it to the result list
        #         result.append("".join(current_string_list))

        # # We start the backtracking process by creating valid strings that start with "0" and "1"
        # create_valid_strings(["0"])
        # create_valid_strings(["1"])

        # # Finally, we return the list of valid binary strings
        # return result

        # We can also solve this problem using bit manipulation. We can generate all possible binary strings of length n and filter out the ones that contain adjacent zeros. To check for adjacent zeros, we can use a bitwise operation to ensure that there are no two consecutive bits that are both 0. We can achieve this by using the expression ((value ^ bit_mask) & ((value ^ bit_mask) >> 1)) == 0, where value is the current binary string represented as an integer and bit_mask is a mask that has all bits set to 1 for the length n. This expression checks if there are any adjacent zeros in the binary representation of value. If any adjacent zeros are present, the expression will evaluate to a non-zero value, and we can filter out those binary strings accordingly.
        # Time complexity: O(n*2^n) in the worst case, as we are generating all possible binary strings of length n and each string takes O(n) time to construct each string from the list of characters using the join operation where n is the length of the string.
        # Space complexity: O(n*2^n) in the worst case, as we are storing all valid binary strings (total 2^n) of length n in the result list, and each string takes O(n) space to store where n is the length of the string.

        # If n is 1, return the valid binary strings of length 1, which are "0" and "1"
        if n == 1:
            return ["0", "1"]
        # If n is 2, return the valid binary strings of length 2, which are "01", "10", and "11"
        elif n == 2:
            return ["01", "10", "11"]
        # For n greater than 2, we generate all possible binary strings of length n and filter out the ones that contain adjacent zeros using bit manipulation
        else:
            # We calculate the end limit for generating binary strings, which is 2^n
            end_limit = 1 << n

            # We create a bit mask that has all bits set to 1 for the length n
            bit_mask = (1 << n) - 1

            # We use a list comprehension to generate all valid binary strings of length n. We iterate through all possible values from 2 to end_limit (exclusive) and check if the binary representation of the value does not contain adjacent zeros using the bitwise expression. If the expression evaluates to 0, it means there are no adjacent zeros, and we format the value as a binary string with leading zeros to ensure it has length n.
            return [
                f"{value:0{n}b}"
                for value in range(2, end_limit)
                if ((value ^ bit_mask) & ((value ^ bit_mask) >> 1)) == 0
            ]


# @lc code=end
