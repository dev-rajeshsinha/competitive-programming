#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
#
# algorithms
# Medium (84.84%)
# Likes:    2025
# Dislikes: 138
# Total Accepted:    140.9K
# Total Submissions: 166K
# Testcase Example:  '[2,3,1,6,7]'
#
# Given an array of integers arr.
#
# We want to select three indices i, j and k where (0 <= i < j <= k <
# arr.length).
#
# Let's define a and b as follows:
#
#
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
#
#
# Note that ^ denotes the bitwise-xor operation.
#
# Return the number of triplets (i, j and k) Where a == b.
#
#
# Example 1:
#
#
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
#
#
# Example 2:
#
#
# Input: arr = [1,1,1,1,1]
# Output: 10
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8
#
#
#

# @lc code=start
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # # The problem requires us to split a subarray arr[i...k] at an index 'j' such that the XOR sum of the left part (a) equals the XOR sum of the right part (b). Because of the properties of XOR, if a == b, then a ^ b = 0. Therefore, instead of looking for three distinct indices, we simply look for a continuous subarray arr[i...k] where the total XOR sum of all its elements is exactly 0.

        # # The 'k - i' Distance Optimization:
        # # If we find a subarray arr[i...k] that XORs to 0, ANY index 'j' chosen strictly between 'i' and 'k' (where i < j <= k) will perfectly split the subarray into two equal-XOR halves. The number of valid split points 'j' is mathematically equal to the distance: (k - i). This realization completely eliminates the need for a third inner loop, bringing the time complexity down from O(N^3) brute force to O(N^2).

        # # Step 1: In-Place Prefix XOR:
        # # We iterate through the array once to convert it into a prefix XOR array in-place. After this step, arr[x] represents the XOR sum of all original elements from index 0 to x.

        # # Step 2: Subarray Evaluation (The Nested Loops):
        # # We use two pointers to define the bounds of every possible subarray:
        # # - 'first_index' acts as our subarray start (i)
        # # - 'second_index' acts as our subarray end (k)

        # # To find the XOR sum of the current subarray in O(1) time, we use the prefix XOR formula:
        # # SubarrayXOR(i, k) = Prefix[k] ^ Prefix[i - 1]

        # # Edge Case Handling: If 'first_index' is 0, the subarray starts at the very beginning of the array, so there is no Prefix[i - 1] to subtract. The XOR sum is simply Prefix[k].

        # # Whenever the evaluated SubarrayXOR equals 0, we instantly add (second_index - first_index) to our total count.
        # # Time Complexity: O(N^2) due to the nested loops, which is efficient for the given constraints (N <= 300).
        # # Space Complexity: O(1) since we are modifying the input array in place and using only a constant amount of extra space for counting.

        # # Calculate the length of the input array
        # n = len(arr)

        # # If the array has fewer than 2 elements, it's impossible to form a valid triplet, so we return 0 immediately.
        # if n < 2:
        #     return 0

        # # Step 1: Compute the prefix XOR in-place. After this loop, arr[index] will hold the XOR of all elements from arr[0] to arr[index].
        # for index in range(1, n):
        #     arr[index] ^= arr[index - 1]

        # # Initialize the count of valid triplets to 0
        # count = 0

        # # Step 2: Use two nested loops to evaluate every possible subarray defined by 'first_index' and 'second_index'.
        # for first_index in range(0, n - 1):
        #     for second_index in range(first_index + 1, n):
        #         # If 'first_index' is 0, the XOR sum of the subarray from 0 to 'second_index' is simply arr[second_index]. We check if it equals 0 and if so, we add 'second_index' to our count (since all indices from 1 to 'second_index' can serve as valid split points).
        #         if first_index == 0:
        #             count += second_index if arr[second_index] == 0 else 0
        #         else:
        #             # For 'first_index' greater than 0, we calculate the XOR sum of the subarray from 'first_index' to 'second_index' using the prefix XOR values. If this XOR sum equals 0, it means all indices between 'first_index' and 'second_index' can serve as valid split points, so we add (second_index - first_index) to our count.
        #             count += (
        #                 second_index - first_index
        #                 if arr[second_index] ^ arr[first_index - 1] == 0
        #                 else 0
        #             )

        # # After evaluating all possible subarrays, we return the total count of valid triplets.
        # return count

        # There is an alternate optimized approach to find the total count of the triplets. The problem asks us to find two adjacent subarrays, arr[i...j-1] (let's call it A) and arr[j...k] (let's call it B), such that A == B. A fundamental property of XOR is that if A == B, then A ^ B == 0. Therefore, we are simply looking for a single combined subarray arr[i...k] where the total XOR sum is exactly 0.

        # The 'k - i' Rule:
        # If a subarray arr[i...k] has an XOR sum of 0, then any index 'j' strictly between 'i' and 'k' (where i < j <= k) forms a valid triplet. The number of valid 'j' splits is exactly (k - i).

        # Prefix XOR & The Hash Map Optimization:
        # To find subarrays that XOR to 0, we track a running prefix XOR. If the prefix XOR at our current index 'k' is identical to a prefix XOR we saw previously at an index 'p', it means the elements strictly between them (from index p+1 to k) XOR to 0. So, our valid subarray starting index is actually i = p + 1.

        # Instead of using a nested loop to look back at every 'p', we use a Hash Map to store:
        # 1. visit_count: How many times we've seen this prefix XOR.
        # 2. index_sum: The sum of all the predicted starting indices (p + 1) for those occurrences.

        # The O(1) Formula:
        # When we encounter a matching prefix XOR at our current index 'k', we calculate the total distance to all previous valid starting indices simultaneously using basic algebra: Total Triplets = (visit_count * k) - index_sum

        # The 'Ghost Zero':
        # We initialize the dictionary with {0: [1, 0]}. This acts as an anchor, pretending we saw a prefix XOR of 0 exactly once before the array started (at an imaginary starting index of 0). This perfectly handles subarrays that XOR to 0 starting from the very first element.
        # Time Complexity: O(N) due to the single pass through the array and O(1) average time for hash map operations.
        # Space Complexity: O(N) in the worst case if all prefix XORs are unique, but typically much less due to repeated XOR values.

        # Calculate the length of the input array
        n = len(arr)

        # If the array has fewer than 2 elements, it's impossible to form a valid triplet, so we return 0 immediately.
        if n < 2:
            return 0

        # Initialize a dictionary to store the count of prefix XOR occurrences and the sum of their predicted starting indices. We start with the 'ghost zero' to handle subarrays that XOR to 0 from the beginning.
        prefix_xor_dict: dict[int, list[int]] = {0: [1, 0]}

        # Initialize the count of valid triplets to 0
        count = 0

        # Iterate through the array from index 0 to n-1 to compute the prefix XOR in-place.
        for index in range(0, n):
            # Compute the prefix XOR for the current index. If index is 0, we XOR with 0 (which does nothing), otherwise we XOR with the previous prefix XOR value.
            arr[index] ^= arr[index - 1] if index > 0 else 0

            # Check if the current prefix XOR value has been seen before in the dictionary.
            if arr[index] in prefix_xor_dict:
                # If it has been seen, we retrieve the visit count and the sum of predicted starting indices for this prefix XOR value.
                visit_count, index_sum = prefix_xor_dict[arr[index]]

                # We calculate the number of new triplets formed by the current index and all previous occurrences of this prefix XOR value using the formula: Total Triplets = (visit_count * current_index) - index_sum
                count += (visit_count * index) - index_sum

                # We then update the dictionary entry for this prefix XOR value by incrementing the visit count and adding the current index + 1 to the index sum (since the predicted starting index for future matches would be current_index + 1).
                prefix_xor_dict[arr[index]][0] += 1
                prefix_xor_dict[arr[index]][1] += index + 1
            else:
                # If this prefix XOR value has not been seen before, we create a new entry in the dictionary with a visit count of 1 and an index sum of current_index + 1.
                prefix_xor_dict[arr[index]] = [1, index + 1]

        # After processing all indices, we return the total count of valid triplets.
        return count


# @lc code=end
