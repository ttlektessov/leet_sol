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
