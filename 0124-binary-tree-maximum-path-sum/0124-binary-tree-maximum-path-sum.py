class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # path through current node
            self.max_sum = max(self.max_sum, left + right + node.val)

            # return max gain to parent
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum