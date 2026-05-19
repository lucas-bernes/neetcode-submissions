class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_arr = s.split()
        return len(word_arr[-1])