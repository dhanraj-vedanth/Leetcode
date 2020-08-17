from symmetric_tree_101.main import (
    Solution,
    TreeNode
    )


def test_symm_tree():
    root = TreeNode(1, None, None)
    lc1 = TreeNode(2, None, None)
    rc1 = TreeNode(2, None, None)
    lc2 = TreeNode(3, None, None)
    lc22 = TreeNode(4, None, None)
    rc2 = TreeNode(4, None, None)
    rc22 = TreeNode(3, None, None)
    root.left = lc1
    root.right = rc1
    lc1.left = lc2
    lc1.right = lc22
    rc1.left = rc2
    rc1.right = rc22

    s = Solution()
    assert (s.isSymmetric(root) is True)
