def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return self.is_mirror(root, root)


def is_mirror(self, t1, t2):
    if (t1 is None and t2 is None):  # if both trees are empty -> return true
        return True
    if (t1 is None or t2 is None):  # if one of the trees are empty -> return false
        return False
    return (t1.val == t2.val and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left,
                                                                                      t2.right))  # check if the value of the nodes are equal recursively. (Mirror each other)
