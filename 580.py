class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        travel = []
        self.traverse(root, travel)
        return travel
    def traverse(self, root, travel):
        if root is None: return
        travel.append(root.val)
        for child in root.children:
            self.traverse(child, travel)
