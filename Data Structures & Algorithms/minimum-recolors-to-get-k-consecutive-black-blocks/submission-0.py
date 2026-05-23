class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = left+k-1
        window = list(blocks[left:right+1])
        minimum_flips = len(window)

        while right < len(blocks):
            count = window.count('W')
            if window.count('W') < minimum_flips:
                minimum_flips = count
            if right == (len(blocks)-1): break
            right += 1
            window.append(blocks[right])
            window.pop(0)
        
        return minimum_flips