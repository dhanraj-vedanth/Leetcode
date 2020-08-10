# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.max_count = 0
        self.caller(root,0)
        return self.max_count
        
    def caller(self, curr_node,count):
        if curr_node.left == None and curr_node.right == None:
            print(count)
            if count > self.max_count:
                self.max_count = count
            return
        
        if curr_node.left != None and curr_node.right != None:
            if curr_node.val == curr_node.left.val and curr_node.val == curr_node.right.val:
                self.caller(curr_node.left,count+2)
                self.caller(curr_node.right,count+2)
        elif curr_node.left != None:
            if curr_node.val == curr_node.left.val:
                self.caller(curr_node.left,count +1)
            else:
                self.caller(curr_node.left,0)
        elif curr_node.right != None:
            if curr_node.val == curr_node.right.val:
                self.caller(curr_node.right,count +1)
            else:
                self.caller(curr_node.right,0)
            
            
        
        