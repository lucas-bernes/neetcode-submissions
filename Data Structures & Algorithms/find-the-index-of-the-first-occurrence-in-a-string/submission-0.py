class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index1 = 0
        index2 = 0
        first_occurrence = -1

        while index1 < len(haystack):
            start_index = index1
            while index2 < len(needle) and index1 < len(haystack):
                if haystack[index1] == needle[index2]:
                    if index2 == (len(needle)-1): 
                        first_occurence = start_index
                        return first_occurence

                    index1 += 1
                    index2 += 1
                
                else:
                    index1 = start_index
                    index2 = 0
                    break
            index1 += 1
        
        return first_occurrence
                
            