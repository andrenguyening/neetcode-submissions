class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        opening_brackets = ['(','[','{']
        bracket_map = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        for c in s:
            if c in opening_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                if bracket_map[c] != stack[-1]:
                    return False               
                stack.pop()
        return not stack
                

