#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#
# https://leetcode.com/problems/richest-customer-wealth/description/
#
# algorithms
# Easy (88.67%)
# Likes:    4854
# Dislikes: 389
# Total Accepted:    1.2M
# Total Submissions: 1.4M
# Testcase Example:  '[[1,2,3],[3,2,1]]'
#
# You are given an m x n integer grid accounts where accounts[i][j] is the
# amount of money the i​​​​​^​​​​​​th​​​​ customer has in the
# j​​​​​^​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank
# accounts. The richest customer is the customer that has the maximum
# wealth.
#
#
# Example 1:
#
#
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return
# 6.
#
#
# Example 2:
#
#
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation:
# 1st customer has wealth = 6
# 2nd customer has wealth = 10
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
#
# Example 3:
#
#
# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17
#
#
#
# Constraints:
#
#
# m == accounts.length
# n == accounts[i].length
# 1 <= m, n <= 50
# 1 <= accounts[i][j] <= 100
#
#
#

# @lc code=start
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # The approach is to iterate through each customer's accounts, calculate their total wealth by summing the amounts in their accounts, and keep track of the maximum wealth encountered. Finally, we return the maximum wealth found. We have used a generator expression to calculate the wealth of each customer and the built-in max function to find the maximum wealth among all customers.
        # Time complexity: O(m*n), where m is the number of customers and n is the number of accounts per customer, since we need to iterate through each customer's accounts to calculate their wealth.
        # Space complexity: O(1), since we are using a constant amount of extra space

        # Return the maximum wealth among all customers
        return max(sum(balances) for balances in accounts)


# @lc code=end
