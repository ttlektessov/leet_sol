class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output =[]
        self.inorder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        
        return True
    
    def inorder(self, root, output):
        if root is None:
            return
        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
