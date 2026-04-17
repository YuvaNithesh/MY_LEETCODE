class Solution:
    def sumOfDistancesInTree(self, n: int, edges):
        from collections import defaultdict
        
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        res = [0] * n
        count = [1] * n
        
        # First DFS: compute subtree sizes and res[0]
        def dfs(node, parent):
            for nei in tree[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
                count[node] += count[nei]
                res[node] += res[nei] + count[nei]
        
        # Second DFS: rerooting
        def dfs2(node, parent):
            for nei in tree[node]:
                if nei == parent:
                    continue
                
                res[nei] = res[node] - count[nei] + (n - count[nei])
                dfs2(nei, node)
        
        dfs(0, -1)
        dfs2(0, -1)
        
        return res