class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True

        for i in range(len(s)):
            if all(s[(i+j) % len(s)] == goal[j] for j in range(len(s))):
                return True
        return False