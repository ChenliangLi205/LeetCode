class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        def satisfy():
            for char, cnt in t2cnt.items():
                if s2cnt.setdefault(char, 0) < cnt:
                    return False
            return True

        if len(s) == 0 or len(t) == 0:
            return ""
        if len(t) > len(s):
            return ""

        t2cnt = dict()
        for char in t:
            if char in t2cnt:
                t2cnt[char] += 1
            else:
                t2cnt[char] = 1
        s2cnt = dict()
        for char in s:
            s2cnt.setdefault(char, 0)
            s2cnt[char] += 1
        if satisfy():
            s2cnt, left, right = dict(), 0, 0
            result = s

            while True:
                if satisfy():
                    if right - left < len(result):
                        result = s[left: right]
                    s2cnt[s[left]] -= 1
                    left += 1
                else:
                    if right == len(s):
                        break
                    right += 1
                    if s[right - 1] not in s2cnt:
                        s2cnt[s[right - 1]] = 0
                    s2cnt[s[right - 1]] += 1
            return result
        else:
            return ""