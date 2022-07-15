# I donnt understand this one, I just copy it
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def diameterOfBinaryTree(root:TreeNode):
    def dfs(root): 
        nonlocal diameter
        if root is None: 
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        
        diameter = max(left + right, diameter)
        
        return max(left, right) + 1
            
                    
    diameter = 0
    dfs(root)
    return diameter
