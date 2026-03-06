#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#
# https://leetcode.com/problems/find-words-containing-character/description/
#
# algorithms
# Easy (90.41%)
# Likes:    690
# Dislikes: 54
# Total Accepted:    384.9K
# Total Submissions: 425.7K
# Testcase Example:  '["leet","code"]\n"e"'
#
# You are given a 0-indexed array of strings words and a character x.
#
# Return an array of indices representing the words that contain the character
# x.
#
# Note that the returned array may be in any order.
#
#
# Example 1:
#
#
# Input: words = ["leet","code"], x = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return
# indices 0 and 1.
#
#
# Example 2:
#
#
# Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
# Output: [0,2]
# Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and
# 2.
#
#
# Example 3:
#
#
# Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
# Output: []
# Explanation: "z" does not occur in any of the words. Hence, we return an
# empty array.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 50
# 1 <= words[i].length <= 50
# x is a lowercase English letter.
# words[i] consists only of lowercase English letters.
#
#
#


# @lc code=start
from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # We can iterate through the list of words and check if the character x is present in each word. If it is, we can add the index of that word to our result list. We can use a list comprehension to achieve this in a concise way along with the enumerate function, which will give us both the index and the word at the same time.
        # Time complexity: O(n * m), where n is the number of words and m is the average length of the words.
        # Space complexity: O(1), since we are only storing the indices of the words

        # Iterate through the list of words and check if x is in each word, returning the indices of the words that contain x.
        return [i for i, v in enumerate(words) if x in v]


# @lc code=end
