class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:len(S) - 1]
        results = []
        for i in range(1, len(S)):
            lefts, rights = [], []
            left, right = S[:i], S[i:]
            if len(left) > 1 and left[0] == '0':
                if left[-1] == '0':
                    continue
                else:
                    lefts.append("%s.%s" % (left[:1], left[1:]))
            else:
                lefts.append(left)
                if len(left) > 1 and left[-1] != '0':
                    for j in range(1, len(left)):
                        lefts.append("%s.%s" % (left[:j], left[j:]))

            if len(right) > 1 and right[0] == '0':
                if right[-1] == '0':
                    continue
                else:
                    rights.append("%s.%s" % (right[:1], right[1:]))
            else:
                rights.append(right)
                if len(right) > 1 and right[-1] != '0':
                    for j in range(1, len(right)):
                        rights.append("%s.%s" % (right[:j], right[j:]))
            for l in lefts:
                for r in rights:
                    results.append("(%s, %s)" % (l, r))
        return results