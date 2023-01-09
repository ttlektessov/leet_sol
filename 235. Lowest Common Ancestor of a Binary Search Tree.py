class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            min_val = p.val
            max_val = q.val
        else:
            min_val = q.val
            max_val = p.val
        while True:
            if min_val <= root.val <= max_val:
                return root
            elif max_val < root.val:
                root = root.left
            else:
                root = root.right
