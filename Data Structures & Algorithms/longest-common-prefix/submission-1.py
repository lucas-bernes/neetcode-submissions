class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs[0]) == 0: return ""

        index_word = 0
        index_letter = 0
        test_prefix = True
        prefix = []

        while test_prefix and index_letter < len(min(strs, key=len)):
            prefix.append(strs[0][index_letter])
            for word in strs:
                if word[index_letter] != prefix[index_letter]:
                    test_prefix = False
                    del prefix[-1]
                    break
                
            if test_prefix == True:
                index_letter += 1
        
        if len(prefix) == 0: return ""
        else: return "".join(prefix)
        
