from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str):
        n = len(ring)

        # map each char to its indices
        pos_map = defaultdict(list)
        for i, ch in enumerate(ring):
            pos_map[ch].append(i)

        @lru_cache(None)
        def dfs(i, pos):
            if i == len(key):
                return 0

            res = float('inf')

            for target in pos_map[key[i]]:
                diff = abs(target - pos)
                step = min(diff, n - diff)  # circular distance

                res = min(res, step + 1 + dfs(i + 1, target))

            return res

        return dfs(0, 0)