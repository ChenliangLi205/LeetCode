class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        left = 0
        right = 10
        DNAset = set()
        ans = set()
        while right <= len(s):
            if s[left:right] in DNAset:
                ans.add(s[left:right])
            else:
                DNAset.add(s[left:right])
            left += 1
            right += 1
        return list(ans)