# 704. Binary Search
# Day 7, 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high, low = len(nums)-1, 0
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

# 278. First Bad Version
# Day 7, 2

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n
        bad = 0
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) == False:
                low = mid+1
            elif isBadVersion(mid) == True:
                high = mid-1
                bad = mid
        return bad
    
# 98. Validate Binary Search Tree
# Day 8, 1

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
    
# Day 8, 2
# 235. Lowest Common Ancestor of a Binary Search Tree
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
# Day 9, 1
# 733. Flood Fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cols = len(image[0])
        rows = len(image)
        color_to_change = image[sr][sc]
        
        def dfs(r, c):
            nonlocal rows, cols, color, image
            
            if r < 0 or c < 0 or r>rows-1 or c>cols-1 or image[r][c]==color or image[r][c]!=color_to_change:
                return
            
            image[r][c] = color
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
 
        dfs(sr, sc)
        return image
        
# Day 9, 2
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
