class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                    continue
            if char == ']':
                if len(stack) and stack[-1] == '[':
                    stack.pop()
                    continue
            if char == '}':
                if len(stack) and stack[-1] == '{':
                    stack.pop()
                    continue
            if char in '()':
                stack.append(char)
            elif char in '[]':
                stack.append(char)
            else:
                stack.append(char)
        return len(stack)==0