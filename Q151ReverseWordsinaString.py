class Solution(object):
    def _split(self, s):
        words = []
        if len(s) == 0:
            return words
        tmp = ""
        for c in s:
            if c == ' ':
                if len(tmp) > 0:
                    words.append(tmp)
                    tmp = ""
            else:
                tmp += c
        if len(tmp) > 0:
            words.append(tmp)
        return words
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        ans = ""
        words = self._split(s)
        if len(words) == 0:
            return ans
        if len(words) == 1:
            return words[0]
        while len(words)>1:
            ans+=words[-1]
            ans += " "
            words.pop(-1)
        ans += words[0]
        return ans