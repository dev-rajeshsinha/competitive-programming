#
# @lc app=leetcode id=3668 lang=python3
#
# [3668] Restore Finishing Order
#
# https://leetcode.com/problems/restore-finishing-order/description/
#
# algorithms
# Easy (91.09%)
# Likes:    109
# Dislikes: 4
# Total Accepted:    92.3K
# Total Submissions: 101.4K
# Testcase Example:  '[3,1,2,5,4]\n[1,3,4]'
#
# You are given an integer array order of length n and an integer array
# friends.
#
#
# order contains every integer from 1 to n exactly once, representing the IDs
# of the participants of a race in their finishing order.
# friends contains the IDs of your friends in the race sorted in strictly
# increasing order. Each ID in friends is guaranteed to appear in the order
# array.
#
#
# Return an array containing your friends' IDs in their finishing order.
#
#
# Example 1:
#
#
# Input: order = [3,1,2,5,4], friends = [1,3,4]
#
# Output: [3,1,4]
#
# Explanation:
#
# The finishing order is [3, 1, 2, 5, 4]. Therefore, the finishing order of
# your friends is [3, 1, 4].
#
#
# Example 2:
#
#
# Input: order = [1,4,5,3,2], friends = [2,5]
#
# Output: [5,2]
#
# Explanation:
#
# The finishing order is [1, 4, 5, 3, 2]. Therefore, the finishing order of
# your friends is [5, 2].
#
#
#
# Constraints:
#
#
# 1 <= n == order.length <= 100
# order contains every integer from 1 to n exactly once
# 1 <= friends.length <= min(8, n)
# 1 <= friends[i] <= n
# friends is strictly increasing
#
#
#

# @lc code=start
from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # We can use a set to store the friends' IDs for O(1) lookups. Then, we can iterate through the order array and check if each ID is in the friends set. If it is, we add it to the result list. This way, we can restore the finishing order of our friends efficiently.
        # Time complexity: O(n+m) where n is the length of the order array and m is the number of friends
        # Space complexity: O(m) where m is the number of friends

        # Use a set for friends for O(1) lookups
        friends_set = set(friends)

        # Iterate through the order array and collect the IDs of friends in their finishing order
        return [f for f in order if f in friends_set]


# @lc code=end
