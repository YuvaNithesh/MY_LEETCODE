from functools import lru_cache

class Solution:
    def allPossibleFBT(self, n: int):
        @lru_cache(None)
        def build(n):
            if n == 1:
                return [TreeNode(0)]
            
            res = []
            
            for left_nodes in range(1, n, 2):
                right_nodes = n - 1 - left_nodes
                
                for left in build(left_nodes):
                    for right in build(right_nodes):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            
            return res
        
        if n % 2 == 0:
            return []
        
        return build(n)