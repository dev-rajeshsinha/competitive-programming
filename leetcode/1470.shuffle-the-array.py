#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#
# https://leetcode.com/problems/shuffle-the-array/description/
#
# algorithms
# Easy (88.95%)
# Likes:    6357
# Dislikes: 350
# Total Accepted:    1M
# Total Submissions: 1.2M
# Testcase Example:  '[2,5,1,3,4,7]\n3'
#
# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#
#
# Example 1:
#
#
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
# [2,3,5,4,1,7].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
#
#
# Example 3:
#
#
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
#
#
#
# Constraints:
#
#
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3
#
#

# @lc code=start
from typing import List


class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # # The approach is to iterate through the first n elements of the array and append the corresponding elements from both first and second halves of the array to the result list. This way, we can achieve the desired interleaving of elements.
        # # Time complexity: O(2n) = O(n), since we are iterating through the array once.
        # # Space complexity: O(2n) = O(n), since we are creating a new list to store the result.

        # # Initialize an empty list to store the result
        # result = []

        # # Iterate through the first n elements of the array
        # for i in range(0, n):
        #     # Append the corresponding elements from both halves of the array to the result list
        #     result.append(nums[i])
        #     result.append(nums[i + n])

        # # Return the interleaved result
        # return result

        # # It is possible to achieve the same result using list comprehension, which can make the code more concise. However, the time and space complexity would remain the same.

        # In this approach, we first create a list of tuples using the zip function, which pairs elements from the first half of the array (nums[:n]) with elements from the second half of the array (nums[n:]). Then, we use a nested list comprehension to flatten the list of tuples into a single list, which gives us the desired interleaved result. The time and space complexity of this approach is also O(n), since we are iterating through the array once and creating a new list to store the result.

        # Return the interleaved result using list comprehension and zip
        # return [value for items in zip(nums[:n], nums[n:]) for value in items]

        # In this approach, we can achieve the interleaving of elements in-place without using extra space for a new list. We can use two pointers to keep track of the current index in the first half and the second half of the array. We can iterate through the array and update the elements at the current index by adding the corresponding elements from both halves of the array, multiplied by a base value (1001 in this case) to ensure that we can retrieve the original values later. After updating all elements, we can divide each element by the base value to get the final interleaved result.
        # Time complexity: O(2n+2n) = O(n), since we are iterating through the array twice.
        # Space complexity: O(1), since we are modifying the array in-place without using extra space.

        # Initialize pointers for the first and second halves of the array
        first_half_start_index = 0
        second_half_start_index = n

        # Use a base value to store the original values while interleaving the elements
        base = 1001

        # Iterate through the array and update the elements at the current index by adding the corresponding elements from both halves of the array, multiplied by the base value
        for i in range(0, 2 * n):
            # If the current index is even, add the corresponding element from the first half of the array
            if i & 1 == 0:
                # Use modulo to retrieve the original value from the current element and add the corresponding element from the first half of the array, multiplied by the base value
                nums[i] += (nums[first_half_start_index] % base) * base

                # Increment the pointer for the first half of the array
                first_half_start_index += 1
            else:
                # If the current index is odd, add the corresponding element from the second half of the array
                # Use modulo to retrieve the original value from the current element and add the corresponding element from the second half of the array, multiplied by the base value
                nums[i] += (nums[second_half_start_index] % base) * base

                # Increment the pointer for the second half of the array
                second_half_start_index += 1

        # After updating all elements, divide each element by the base value to get the final interleaved result
        for i in range(0, 2 * n):
            # Divide each element by the base value to retrieve the original value and get the final interleaved result
            nums[i] //= base

        # Return the interleaved result
        return nums


# @lc code=end
