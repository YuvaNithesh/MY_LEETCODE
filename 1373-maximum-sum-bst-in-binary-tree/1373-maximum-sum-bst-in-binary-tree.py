class Solution:
    def maxSumBST(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            
            l_is_bst, l_min, l_max, l_sum = dfs(node.left)
            r_is_bst, r_min, r_max, r_sum = dfs(node.right)
            
            if l_is_bst and r_is_bst and l_max < node.val < r_min:
                curr_sum = l_sum + r_sum + node.val
                self.ans = max(self.ans, curr_sum)
                return (True,
                        min(l_min, node.val),
                        max(r_max, node.val),
                        curr_sum)
            
            return (False, 0, 0, 0)
        
        dfs(root)
        return self.ans