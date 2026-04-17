class Solution:
    def minCameraCover(self, root):
        self.cameras = 0
        
        def dfs(node):
            if not node:
                return 2  # null nodes are covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If any child is not covered → place camera
            if left == 0 or right == 0:
                self.cameras += 1
                return 1
            
            # If any child has camera → covered
            if left == 1 or right == 1:
                return 2
            
            # Otherwise → not covered
            return 0
        
        # If root is not covered → add camera
        if dfs(root) == 0:
            self.cameras += 1
        
        return self.cameras