#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#
# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
#
# algorithms
# Medium (89.80%)
# Likes:    1762
# Dislikes: 123
# Total Accepted:    306.1K
# Total Submissions: 340.8K
# Testcase Example:  '[9,12,5,10,14,3,10]\n10'
#
# You are given a 0-indexed integer array nums and an integer pivot. Rearrange
# nums such that the following conditions are satisfied:
#
#
# Every element less than pivot appears before every element greater than
# pivot.
# Every element equal to pivot appears in between the elements less than and
# greater than pivot.
# The relative order of the elements less than pivot and the elements greater
# than pivot is maintained.
#
# More formally, consider every pi, pj where pi is the new position of the i^th
# element and pj is the new position of the j^th element. If i < j and both
# elements are smaller (or larger) than pivot, then pi < pj.
#
#
#
#
# Return nums after the rearrangement.
#
#
# Example 1:
#
#
# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]
# Explanation:
# The elements 9, 5, and 3 are less than the pivot so they are on the left side
# of the array.
# The elements 12 and 14 are greater than the pivot so they are on the right
# side of the array.
# The relative ordering of the elements less than and greater than pivot is
# also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
#
#
# Example 2:
#
#
# Input: nums = [-3,4,3,2], pivot = 2
# Output: [-3,2,4,3]
# Explanation:
# The element -3 is less than the pivot so it is on the left side of the array.
# The elements 4 and 3 are greater than the pivot so they are on the right side
# of the array.
# The relative ordering of the elements less than and greater than pivot is
# also maintained. [-3] and [4, 3] are the respective orderings.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^6 <= nums[i] <= 10^6
# pivot equals to an element of nums.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # # The approach is to create three separate lists: one for elements less than the pivot, one for elements equal to the pivot, and one for elements greater than the pivot. We then concatenate these lists together to get the final result.
        # # Time complexity: O(n), where n is the length of the input array nums, since we need to iterate through the array once to partition the elements.
        # # Space complexity: O(n), since we are creating three separate lists to hold the partitioned elements, which in the worst case can hold all the elements of the input array.

        # # Create three separate lists to hold the partitioned elements
        # less_than_pivot: List[int] = []
        # equal_to_pivot: List[int] = []
        # greater_than_pivot: List[int] = []

        # # Iterate through the input array and partition the elements based on their relation to the pivot
        # for i in nums:
        #     if i < pivot:
        #         less_than_pivot.append(i)
        #     elif i == pivot:
        #         equal_to_pivot.append(i)
        #     else:
        #         greater_than_pivot.append(i)

        # # Concatenate the three lists together to get the final result and return it
        # return less_than_pivot + equal_to_pivot + greater_than_pivot

        # Apart from creating three separate lists, another optimization can be done by counting the number of equal to and greater than the pivot in a single pass through the input array. We can then create a new result array and create the positional pointers for the three partitions based on the counts. Finally, we can iterate through the input array again and place the elements in their respective positions in the result array based on their relation to the pivot. In this way, we can eliminate the need for three separate lists and reduce the space complexity to O(n) for the result array only.
        # Time complexity: O(n), where n is the length of the input array nums, since we need to iterate through the array twice: once to count the elements and once to place them in the result array.
        # Space complexity: O(n), since we are creating a new result array to hold the partitioned elements, which in the worst case can hold all the elements of the input array.

        # Count the number of elements equal to and greater than the pivot
        elements_equal_to_pivot = elements_greater_than_pivot = 0

        # Iterate through the input array and count the number of elements equal to and greater than the pivot
        for num in nums:
            if num == pivot:
                elements_equal_to_pivot += 1
            elif num > pivot:
                elements_greater_than_pivot += 1

        # Create a new result array to hold the partitioned elements
        result: List[int] = [0] * len(nums)

        # Create positional pointers for the three partitions based on the counts
        less_than_pointer_pos = 0
        equal_to_pointer_pos = len(nums) - (
            elements_equal_to_pivot + elements_greater_than_pivot
        )
        greater_than_pointer_pos = equal_to_pointer_pos + elements_equal_to_pivot

        # Iterate through the input array again to place the elements in their respective positions in the result array based on their relation to the pivot
        for num in nums:
            # If the current number is less than the pivot, place it in the position pointed to by less_than_pointer_pos and increment the pointer
            if num < pivot:
                result[less_than_pointer_pos] = num
                less_than_pointer_pos += 1
            # If the current number is equal to the pivot, place it in the position pointed to by equal_to_pointer_pos and increment the pointer
            elif num == pivot:
                result[equal_to_pointer_pos] = num
                equal_to_pointer_pos += 1
            # If the current number is greater than the pivot, place it in the position pointed to by greater_than_pointer_pos and increment the pointer
            else:
                result[greater_than_pointer_pos] = num
                greater_than_pointer_pos += 1

        # Return the final result array after partitioning the elements according to the pivot and maintaining their relative order within their respective partitions
        return result


# @lc code=end
