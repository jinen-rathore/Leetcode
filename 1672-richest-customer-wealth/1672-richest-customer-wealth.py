class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = 0
        for i in accounts:
            b = 0
            for j in i:
                b += j
            a = max(a,b)
        return a