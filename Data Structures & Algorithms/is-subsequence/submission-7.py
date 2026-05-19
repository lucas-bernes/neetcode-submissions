class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if len(s) == 0: return True

        i=0 #index of s
        j=0 #index of t

        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i+=1
            j+=1

        return i == len(s)