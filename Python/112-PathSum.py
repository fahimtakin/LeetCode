class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            if not node:  # if no node is there, return false
                return False
            currentSum += node.val
            if not node.left and not node.right:  # if it's a leaf node
                return currentSum == targetSum
            return (dfs(node.left, currentSum) or dfs(node.right,
                                                      currentSum))  # if not leaf node then call left and right subtree recursively

        return dfs(root, 0)  # call the dfs function
