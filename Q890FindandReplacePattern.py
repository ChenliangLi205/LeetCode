class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def all_same(a):
            if len(a.replace(a[0], '')) == 0:
                return True
            else:
                return False
        fit_words = []
        pattern_letter2loc = {}

        for i, p in enumerate(pattern):
            if p not in pattern_letter2loc.keys():
                pattern_letter2loc[p] = [i]
            else:
                pattern_letter2loc[p].append(i)

        for word in words:
            fit = True
            for key in pattern_letter2loc.keys():
                letters = ''.join([word[i] for i in pattern_letter2loc[key]])
                if not all_same(letters):
                    fit = False
                    break
            if fit:
                word_key = {j: i for i, j in enumerate(word)}
                if len(word_key) == len(pattern_letter2loc):
                    fit_words.append(word)

        return fit_words