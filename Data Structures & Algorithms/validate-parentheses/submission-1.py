class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        open_stack = []

        for character in s:
            if character in pairs:
                open_stack.append(character)
            else:
                if not open_stack or character != pairs[open_stack[-1]]:
                    return False
                else:
                    open_stack.pop(-1)
        
        return len(open_stack) == 0
