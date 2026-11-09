from math import gcd
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for num in nums:
            new_dp = defaultdict(int)

            for (g1, g2), ways in dp.items():

                # Choice 1: Skip the current element
                new_dp[(g1, g2)] += ways

                # Choice 2: Add to seq1
                new_g1 = gcd(g1, num)
                new_dp[(new_g1, g2)] += ways

                # Choice 3: Add to seq2
                new_g2 = gcd(g2, num)
                new_dp[(g1, new_g2)] += ways

            # Apply modulo
            for state in new_dp:
                new_dp[state] %= MOD

            dp = new_dp

        ans = 0

        # Both subsequences must be non-empty
        for (g1, g2), ways in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + ways) % MOD

        return ans