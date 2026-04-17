class Solution:
    def longestZigZag(self, root):
        self.ans = 0
        
        def dfs(node):
            if not node:
                return (-1, -1)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            left_len = left[1] + 1
            right_len = right[0] + 1
            
            self.ans = max(self.ans, left_len, right_len)
            
            return (left_len, right_len)
        
        dfs(root)
        return self.ans