# 1.intuition - naive - that is just a simple linked list(wrong)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sortedArrayToBST(nums:list):
    root_index = len(nums) // 2
    if root_index == 0:
        return TreeNode(nums[root_index])

    root = TreeNode(nums[root_index])
    temp = root
    for i in range(root_index -1, -1, -1):
        root.left = TreeNode(nums[i])
        root = root.left

    root = temp
    for i in range(root_index+1 , len(nums)):
        root.right = TreeNode(nums[i])
        root = root.right
    
    return temp

print(sortedArrayToBST([0,1,2,3,4,5]))

    