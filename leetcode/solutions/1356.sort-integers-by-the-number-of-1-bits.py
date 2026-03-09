#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/
#
# algorithms
# Easy (82.20%)
# Likes:    2858
# Dislikes: 137
# Total Accepted:    390.1K
# Total Submissions: 474.2K
# Testcase Example:  '[0,1,2,3,4,5,6,7,8]'
#
# You are given an integer array arr. Sort the integers in the array in
# ascending order by the number of 1's in their binary representation and in
# case of two or more integers have the same number of 1's you have to sort
# them in ascending order.
#
# Return the array after sorting it.
#
#
# Example 1:
#
#
# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explanation: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]
#
#
# Example 2:
#
#
# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explanation: All integers have 1 bit in the binary representation, you should
# just sort them in ascending order.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^4
#
#
#

# @lc code=start
from typing import List
from math import inf
from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # # The approach is to create a dictionary where the keys are the number of set bits and the values are lists of integers that have those many number of set bits. We will also keep track of the maximum and minimum number of set bits encountered. Finally, we will iterate through the range of set bit counts from minimum to maximum, sort the corresponding lists of integers, and extend the result array with these sorted lists.
        # # Time complexity: O(n log n) due to the sorting step, where n is the number of integers in the input array.
        # # Space complexity: O(n) for the dictionary that stores the integers based on their set bit counts.

        # # Create a dictionary to store integers based on their number of set bits
        # count_dict: dict[int, list[int]] = {}

        # # Initialize variables to track the maximum and minimum number of set bits
        # max_number_of_bits = -inf
        # min_number_of_bits = inf

        # # Iterate through each integer in the input array
        # for val in arr:
        #     # Calculate the number of set bits in the binary representation of the integer
        #     number_of_set_bits = val.bit_count()

        #     # Add the integer to the corresponding list in the dictionary based on its number of set bits
        #     if number_of_set_bits in count_dict:
        #         count_dict[number_of_set_bits].append(val)
        #     else:
        #         count_dict[number_of_set_bits] = [val]

        #     # Update the maximum and minimum number of set bits encountered
        #     max_number_of_bits = max(max_number_of_bits, number_of_set_bits)
        #     min_number_of_bits = min(min_number_of_bits, number_of_set_bits)

        # # Initialize an array to store the sorted integers
        # arr = []

        # # Iterate through the range of set bit counts from minimum to maximum
        # for set_bit_count in range(
        #     int(min_number_of_bits), int(max_number_of_bits + 1)
        # ):
        #     # If there are integers with the current number of set bits, sort them and extend the result array
        #     if set_bit_count in count_dict.keys():
        #         arr.extend(sorted(count_dict[set_bit_count]))

        # # Return the sorted array
        # return arr

        # # We can also sort the array in-place using a custom sorting key that sorts first by the number of set bits and then by the integer value itself. This approach is more concise and efficient.
        # # Time complexity: O(n log n) due to the sorting step, where n is the number of integers in the input array.
        # # Space complexity: O(1) for the in-place sorting.

        # # Even though the time complexity is the same as the previous approach, this method is more efficient as it does not need to create an additional dictionary to store the integers based on their set bit counts, which completely removed the requirement of hashing and the associated overhead. The built-in sorting algorithm is optimized (uses the underlying implementations written in C) and will handle the sorting efficiently based on the custom key provided. So, in reality, this approach will produce the result faster than the previous one, especially for larger input sizes.

        # # Sort the array in-place using a custom sorting key that sorts first by the number of set bits and then by the integer value itself if there are ties in the number of set bits and return the sorted array
        # arr.sort(key=lambda x: (x.bit_count(), x))
        # return arr

        # This is another approach to solve the problem in O(n) time complexity. It's worth mentioning that, this approach is only possible as the maximum value of the integers in the input array is limited to 10^4, which allows us to use a counting sort-like method based on the number of set bits. The idea is to create a frequency list to count the occurrences of each integer in the input array, then create a dictionary to group integers by their number of set bits, and finally construct the sorted array based on the grouped integers. As we will be filing the frequency list first, and then filling the dictionary from the frequency list sequentially, the integers will be added to the dictionary in sorted order, so we don't need to sort the lists of integers for each set bit count.
        # Time complexity: O(n + m) where n is the number of integers in the input array and m is the range of possible integer values (in this case, m = 10^4).
        # Space complexity: O(m) for the frequency list and the dictionary that stores the integers based on their set bit counts.

        # Create a frequency list to count the occurrences of each integer in the input array
        frequency_list = [0] * ((10**4) + 1)

        # Fill the frequency list based on the input array
        for num in arr:
            frequency_list[num] += 1

        # Create a dictionary to store integers based on their number of set bits
        set_bit_count_dict: defaultdict[int, list[int]] = defaultdict(list)

        # Initialize variables to track the maximum and minimum number of set bits
        min_set_bit_count = inf
        max_set_bit_count = -inf

        # Iterate through the frequency list
        for num, count in enumerate(frequency_list):
            # Check if the current integer has a non-zero frequency in the input array, which means it is present in the input array
            if count > 0:
                # Calculate the number of set bits in the binary representation of the integer
                set_bit_count = num.bit_count()

                # Update the minimum and maximum number of set bits encountered
                min_set_bit_count = min(min_set_bit_count, set_bit_count)
                max_set_bit_count = max(max_set_bit_count, set_bit_count)

                # Add the integer to the corresponding list in the dictionary based on its number of set bits, and repeat it according to its frequency in the input array
                set_bit_count_dict[set_bit_count].extend([num] * count)

        # Initialize an array to store the sorted integers
        arr = []

        # Iterate through the range of set bit counts from minimum to maximum
        for bit_count in range(int(min_set_bit_count), int(max_set_bit_count) + 1):
            # If there are integers with the current number of set bits, extend the result array with these integers (they are already in sorted order due to the way we filled the dictionary from the frequency list)
            if bit_count in set_bit_count_dict:
                arr.extend(set_bit_count_dict[bit_count])

        # Return the sorted array
        return arr


# @lc code=end
