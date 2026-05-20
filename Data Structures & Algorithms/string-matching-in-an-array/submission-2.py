class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        i = 0
        if set(words) == 1: return words[0]

        sub_words = []

        while i < len(words): 
            j=0
            while j < len(words): 
                if words[j] in words[i]:
                    if words[j] == words[i]:
                        j+=1
                        continue
                    sub_words.append(words[j])
                j+=1
            i+=1
        return list(set(sub_words))
