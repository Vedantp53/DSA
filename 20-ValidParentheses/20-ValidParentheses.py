# Last updated: 5/8/2026, 3:50:08 AM
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closed_open = {")":"(","]":"[","}":"{"}

        for c in s:
            if c in closed_open:
                if stack and stack[-1] == closed_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False