class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        files = path.split('/')
        stack = list()
        for f in files:
            if len(f) == 0 or f == '.':
                continue
            elif f == '..':
                if len(stack):
                    stack.pop()
                else:
                    continue
            else:
                stack.append(f)
        return '/'+'/'.join(stack)