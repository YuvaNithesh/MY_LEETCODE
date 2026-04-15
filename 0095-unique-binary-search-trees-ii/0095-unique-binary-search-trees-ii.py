class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]

            trees = []

            for i in range(start, end + 1):
                left_subtrees = build(start, i - 1)
                right_subtrees = build(i + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)   # use LeetCode's TreeNode
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)