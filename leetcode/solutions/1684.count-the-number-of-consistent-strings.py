#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#
# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
#
# algorithms
# Easy (88.48%)
# Likes:    2270
# Dislikes: 90
# Total Accepted:    436.8K
# Total Submissions: 493.7K
# Testcase Example:  '"ab"\n["ad","bd","aaab","baa","badab"]'
#
# You are given a string allowed consisting of distinct characters and an array
# of strings words. A string is consistent if all characters in the string
# appear in the string allowed.
#
# Return the number of consistent strings in the array words.
#
#
# Example 1:
#
#
# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain
# characters 'a' and 'b'.
#
#
# Example 2:
#
#
# Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.
#
#
# Example 3:
#
#
# Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^4
# 1 <= allowed.length <=^ 26
# 1 <= words[i].length <= 10
# The characters in allowed are distinct.
# words[i] and allowed contain only lowercase English letters.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # # The approach is to create a set of allowed characters for O(1) lookups, and then iterate through each word in the words list. For each word, we check if all characters in the word are present in the set of allowed characters. If they are, we increment our count of consistent strings. Finally, we return the count of consistent strings.
        # # Time complexity: O(m*n), where m is the number of words and n is the average length of the words, since we need to check each character of each word against the set of allowed characters.
        # # Space complexity: O(k), where k is the number of distinct characters in the allowed string, since we are storing the allowed characters in a set.

        # # Initialize a counter for consistent strings
        # count_of_consistent_string = 0

        # # Create a set of allowed characters for O(1) lookups
        # set_of_allowed_chars = set(allowed)

        # # Iterate through each word in the words list
        # for word in words:
        #     # Check if all characters in the word are present in the set of allowed characters
        #     for char in word:
        #         # If a character is not in the set of allowed characters, break out of the loop and move to the next word
        #         if char not in set_of_allowed_chars:
        #             break
        #     else:
        #         # If we didn't break out of the loop, it means all characters in the word are allowed, so we increment our count of consistent strings
        #         count_of_consistent_string += 1

        # # Return the count of consistent strings
        # return count_of_consistent_string

        # We can solve this problem more concisely using a generator expression inside the sum function. The generator expression will check if all characters in each word are present in the set of allowed characters, and sum will count how many words are consistent. The `all` function will return True if all characters in the word are in the set of allowed characters, and False otherwise. The sum will then count how many times this is True across all words as the boolean True is treated as 1 and False as 0, so we get the count of consistent strings.
        # Time complexity: O(m*n), where m is the number of words and n is the average length of the words, since we need to check each character of each word against the set of allowed characters.
        # Space complexity: O(k), where k is the number of distinct characters in the allowed string, since we are storing the allowed characters in a set.

        # Create a set of allowed characters for O(1) lookups
        set_of_allowed_chars = set(allowed)

        # Use a generator expression to count how many words are consistent with the allowed characters and return the count
        return sum(all(char in set_of_allowed_chars for char in word) for word in words)


# @lc code=end
