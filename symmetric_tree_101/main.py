from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Iterative way: Doing a BFS
        """
        # qu = deque([(root.left, root.right)])
        # while qu:
        #     lt, rt = qu.popleft()
        #     if lt is None and rt is None:
        #         continue
        #     if lt is None or rt is None:
        #         return False
        #     if lt.val != rt.val:
        #         return False
        #     qu.append((lt.left, rt.right))
        #     qu.append((lt.right, rt.left))
        # return True

        """
        recursive way: DFS for sure
        Can we try doing this using a stack?
        """
        if root is None:
            return True
        return self.check_symmertry(root.left, root.right)

    def check_symmertry(self, lt, rt):
        if lt is None and rt is None:
            return True
        if lt is None or rt is None:
            return False
        return (
            lt.val == rt.val and
            self.check_symmertry(lt.left, rt.right) and
            self.check_symmertry(lt.right, rt.left)
        )
