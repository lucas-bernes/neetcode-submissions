class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        sum = 0
        while i < (len(s)-1):
            print(i,i+1)
            sum = sum + abs(ord(s[i])-ord(s[i+1]))
            i+=1

        return sum