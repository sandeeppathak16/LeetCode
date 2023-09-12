class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0

        for i in range(len(s)):
            string = set()
            for j in range(i, len(s)):
                if s[j] in string:
                    break
                
                string.add(s[j])
            
            ans = max(ans, len(string))
        
        return ans

        