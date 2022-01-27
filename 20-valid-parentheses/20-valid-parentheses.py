class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        match={
        ')':'(',
        '}':'{',
        ']':'['
        }
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
                continue
            if len(stack)==0 or match[s[i]]!=stack.pop():
                return False
        return len(stack)==0