# Last updated: 5/8/2026, 3:50:13 AM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        res = 0
        
        for i in range(len(s)):
            # If this is the subtractive case (smaller value before larger value)
            if (i + 1 < len(s)) and (roman[s[i]] < roman[s[i + 1]]):
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
                
        return res