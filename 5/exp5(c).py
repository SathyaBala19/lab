class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    result = []
    
    def dfs(node, path):
        if not node:
            return
        if not node.left and not node.right:  
            result.append(path + str(node.val))
        else:
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")
    
    dfs(root, "")
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print("All root-to-leaf paths:", binaryTreePaths(root))
