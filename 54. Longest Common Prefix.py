class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        
        i = 0
        for i, chars in enumerate(zip(*strs), 1):
            if len(set(chars)) != 1:
                i -= 1
                break
        
        return strs[0][:i]
