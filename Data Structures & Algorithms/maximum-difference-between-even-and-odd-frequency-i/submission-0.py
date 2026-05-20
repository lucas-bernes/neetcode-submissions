class Solution:
    def maxDifference(self, s: str) -> int:
        
        letters_frequency = {}
        for letter in s:
            letters_frequency[letter] = letters_frequency.get(letter,0) + 1
        
        a1 = max(freq for freq in letters_frequency.values() if freq%2 == 1)
        a2 = min(freq for freq in letters_frequency.values() if freq%2 == 0)

        return a1-a2