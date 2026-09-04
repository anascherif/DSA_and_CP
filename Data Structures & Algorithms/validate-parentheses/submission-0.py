class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        clo = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in clo:
                if stack and stack[-1] == clo[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0