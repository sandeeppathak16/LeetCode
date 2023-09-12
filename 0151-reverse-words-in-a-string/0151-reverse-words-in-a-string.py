class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        
        for string in s.split(' ')[::-1]:
            if string:
                ans.append(string)

        return ' '.join(ans)
        