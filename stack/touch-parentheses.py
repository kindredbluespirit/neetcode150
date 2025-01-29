class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '{','[']
        closing = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        for c in s:
            if c in opening:
                stack.append(c)
            elif len(stack) == 0 or c != closing[stack[-1]]:
                return False
            else:
                stack = stack[:-1]
        
        ## if any braces are left that are not closed after parsing the string
        if len(stack) != 0:
            return False

        return True

