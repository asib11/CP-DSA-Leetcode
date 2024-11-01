class Solution:
    def makeFancyString(self, s: str) -> str:
        new_s = s[:2]
        for i in range(2,len(s)):
            if s[i]== s[i-1] and s[i-1]==s[i-2]:
                pass
            else:
                new_s += s[i]
        return new_s

        
